from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('download', views.show_yt_details, name='show_yt_details'),
    path('download/download_yt_mp3', views.download_yt_mp3, name='download_yt_mp3'),
]
