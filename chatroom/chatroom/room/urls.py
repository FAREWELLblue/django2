from django.conf.urls import url

from room import views

urlpatterns=[
    url(r'^index$',views.index),
    url(r'^room$',views.room),
    url(r'chat$',views.chat),
    url(r'upload$',views.upload),
    url(r'files$',views.files),
    url(r'leave$',views.leave),
]