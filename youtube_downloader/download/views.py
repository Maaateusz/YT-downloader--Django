import os
from time import sleep
from django.http import HttpResponse
from django.template import loader
from .models import DownloadHistory, DownloadItem
from pytube import YouTube
from django.http import JsonResponse
from datetime import timedelta
import json
import io
from pydub import AudioSegment
from django.utils import timezone
from django.http import HttpResponse
from django.http import FileResponse
from django.utils.text import get_valid_filename


def index(request):

    # all
    # showDownloads = DownloadHistory.objects.all().order_by('-downlod_date').values()

    # last 10
    showDownloads = DownloadHistory.objects.all().order_by(
        '-downlod_date').values()[:10]

    # today
    # showDownloads = DownloadHistory.objects.filter(downlod_date__date=date.today()).order_by('-downlod_date').values()

    # od - do
    # start_date = datetime.now()
    # end_date = start_date - timedelta(days=1)
    # showDownloads = DownloadHistory.objects.filter(downlod_date__range=(end_date, start_date)).order_by('-downlod_date').values()

    template = loader.get_template('index.html')
    context = {
        'showDownloads': showDownloads,
    }
    return HttpResponse(template.render(context, request))


def get_file(request):
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

    context = {
        'url': url,
        'title': yt_file.title,
        'author': yt_file.author,
        'views': yt_file.views,
        'thumbnail_url': yt_file.thumbnail_url,
        'publish_date': yt_file.publish_date,
        'length': str(timedelta(seconds=int(yt_file.length))),  # sec
        'description': yt_file.description,
        'streams_video': streams_video,
        'streams_audio': streams_audio,
    }
    return HttpResponse(template.render(context, request))


def addDownloadHistory(request):
    if request.method == 'PUT':
        print(json.loads(request.body))
        request = json.loads(request.body)
        title = request.get('title')
        author = request.get('author')
        url = request.get('url')
        thumbnail_url = request.get('thumbnail_url')
        downloadHistory: DownloadHistory = DownloadHistory(
            downlod_date=timezone.now(),
            file_title=title,
            file_author=author,
            file_url=url,
            thumbnail_url=thumbnail_url)
        print(downloadHistory.file_title)
        print(downloadHistory.downlod_date)

        # save
        downloadHistory.save()

        return JsonResponse({"downloaded_at": downloadHistory.downlod_date})


def get_mp3(request):
    if request.method == 'POST':
        itag = int(json.loads(request.body).get('itag'))
        url = json.loads(request.body).get('url')

        yt = YouTube(url)
        stream = yt.streams.get_by_itag(itag)
        buffer = io.BytesIO()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)
        media_path = "download/media/"
        filename = yt.title + ".mp3"

        # nazwa pliku nie może mieć pewnych znaków
        filename = ''.join(
            filter(lambda x: x.isalnum() or x in "._- ", filename))
        # filename = get_valid_filename(filename)

        AudioSegment.from_file(buffer).export(media_path + filename,
                                              format='mp3',
                                              tags={
                                                  'artist': yt.author,
                                                  'title': yt.title,
                                                  'album': 'From YT',
                                                  'comments': 'Downloaded'
                                              })

        if os.path.exists(media_path + filename):
            response = FileResponse(open(media_path + filename, 'rb'),
                                    as_attachment=True,
                                    filename=filename)
            response['Content-Type'] = "audio/mpeg"
            response['Content-Transfer'] = 'Encoding: binary'
            response['Content-Description'] = 'File Transfer'
            response['Filename'] = filename
            response['Content-Length'] = os.path.getsize(media_path + filename)

            # print(f"{itag} : {filename}")

            return response

    if request.method == 'DELETE':
        filename = json.loads(request.body).get('filename')
        media_path = "download/media/"
        # print(filename)
        # print(media_path)
        clean_media(10, media_path + filename)
        return HttpResponse()


def clean_media(time_sec: int, file_path: str):
    if os.path.exists(file_path):
        for i in range(0, time_sec):
            sleep(1)
            # print(i)
        os.remove(file_path)
        print('=====================removed===============')
    else:
        print("The file does not exist")
