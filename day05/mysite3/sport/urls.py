from django.conf.urls import url

from sport import views

urlpatterns=[
    url(r'^index', views.index_view),
]