from django.conf.urls import url

from news import views

urlpatterns=[
    url(r'^index', views.index_view),
]