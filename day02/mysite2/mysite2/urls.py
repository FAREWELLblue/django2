"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/person/xiaoming/20
    # 命名分组--> 关键字传参
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',views.person_view),
    # http://127.0.0.1:8000/birthday/2015/12/11
    url(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})',views.birthday_view),
    url(r'^birthday/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})',views.birthday_view),

    url(r'^test_get',views.test_get),
    url(r'^test_post',views.test_post),



    url(r'^test_html$',views.test_html),
    url(r'^mycal$',views.mycal)
]
