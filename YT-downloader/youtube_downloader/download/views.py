import os
from time import sleep
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import DownloadItem
from pytube import YouTube
from datetime import timedelta
import json
import io
from pydub import AudioSegment
from django.http import HttpResponse
from django.http import FileResponse
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_PATH = BASE_DIR / 'download/media/'


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def show_yt_details(request):
    url = request.POST['url']
    template = loader.get_template('download.html')

    yt_file = YouTube(url)
    streams_video = list(
        map(
            DownloadItem,
            yt_file.streams.filter(
                mime_type="video/mp4").order_by('resolution').desc()))
    streams_audio = list(
        map(DownloadItem,
            yt_file.streams.filter(only_audio=True).order_by('abr').desc()))

    file_length = str(timedelta(seconds=int(yt_file.length)))

    context = {
        'url': url,
        'title': yt_file.title,
        'author': yt_file.author,
        'views': yt_file.views,
        'thumbnail_url': yt_file.thumbnail_url,
        'publish_date': yt_file.publish_date,
        'length': file_length,
        'isTooLong': yt_file.length > 60 * 90,  # 90 min
        'description': yt_file.description,
        'streams_video': streams_video,
        'streams_audio': streams_audio,
    }

    return HttpResponse(template.render(context, request))


def download_yt_mp3(request):
    if request.method == 'POST':
        itag = int(json.loads(request.body).get('itag'))
        url = json.loads(request.body).get('url')

        # TODO przekazać cały stream ?
        yt = YouTube(url)
        stream = None

        if json.loads(request.body).get('isSimpleDownload') == 'false':
            stream = yt.streams.get_by_itag(itag)
        else:
            stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

        if yt.length > 60 * 90:
            return JsonResponse({'Error': 'File is too long!!!'});

        buffer = io.BytesIO()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)

        filename = clean_filename(yt.title + ".mp3")

        AudioSegment.from_file(buffer).export(MEDIA_PATH / filename,
                                              format='mp3',
                                              tags={
                                                  'artist': yt.author,
                                                  'title': yt.title,
                                                  'album': 'From YT',
                                                  'comments': 'Downloaded'
                                              })

        if os.path.exists(MEDIA_PATH / filename):
            response = FileResponse(open(MEDIA_PATH / filename, 'rb'),
                                    as_attachment=True,
                                    filename=filename)
            response['Content-Type'] = "audio/mpeg"
            response['Content-Transfer'] = 'Encoding: binary'
            response['Content-Description'] = 'File Transfer'
            response['Filename'] = filename
            response['Content-Length'] = os.path.getsize(MEDIA_PATH / filename)
            print(f"{itag} : {filename}")
            return response
    if request.method == 'DELETE':
        filename = clean_filename(json.loads(request.body).get('filename'))
        clean_media(10, MEDIA_PATH / filename)
        return HttpResponse()


def clean_media(time_sec: int, file_path: str):
    if os.path.exists(file_path):
        sleep(time_sec)
        os.remove(file_path)
        print('removed: ' + str(file_path))
    else:
        print("The file does not exist")


def clean_filename(filename):
    return ''.join(filter(lambda x: x.isalnum() or x in "._- ", filename))
