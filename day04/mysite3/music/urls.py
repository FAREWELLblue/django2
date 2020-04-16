from django.conf.urls import url

from music import views

urlpatterns=[
    url(r'^index',views.index_view)
]