from . import views
from django.urls import path
from django.conf.urls import handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('download', views.get_file, name='get_file'),
    path('download/add', views.addDownloadHistory, name='addDownloadHistory'),
    path('download/get_mp3', views.get_mp3, name='get_mp3'),
]
