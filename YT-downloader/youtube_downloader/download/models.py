from typing import Optional
from django.db import models
from pytube import Stream
from django.http import FileResponse
# Create your models here.

class DownloadHistory(models.Model):
    downlod_date = models.DateTimeField()
    file_title = models.CharField(max_length=255)
    file_author = models.CharField(max_length=100)
    file_url = models.URLField()
    thumbnail_url = models.URLField()

class DownloadItem:
    def __init__(self, sq: Stream):
        self.type = sq.type
        self.url = sq.url
        self.subtype = sq.subtype
        self.resolution = sq.resolution
        self.mime_type = sq.mime_type
        self.itag = sq.itag
        self.filesize = sq.filesize
        # self.filesize = sq.filesize()
        self.codecs = sq.codecs
        self.bitrate = sq.bitrate
        self.abr = sq.abr
        self.fps = getattr(sq, 'fps', None)
        self.audio_codec = sq.audio_codec
        self.video_codec = sq.video_codec

