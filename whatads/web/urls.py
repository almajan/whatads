from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/send/txt/$', views.send_messages, name='send text messages'),
    url(r'^api/send/img/$', views.send_images, name='send text messages'),
    url(r'^api/send/vdo/$', views.send_videos, name='send text messages'),
    url(r'^api/send/vce/$', views.send_voices, name='send text messages'),
    url(r'^api/send/dlvy/$', views.check_delivery, name='send text messages'),
    url(r'^api/send/seen/$', views.check_seen, name='send text messages'),

]
