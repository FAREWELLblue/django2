"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('index.urls')),
    url(r'^ranking.html', include('ranking.urls')),
    url(r'^play/', include('play.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^user/', include('user.urls')),
    # 定义静态资源的路由信息
    url('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # 定义媒体资源的路由信息
    url('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
]


# from index import views
#
# handler404 = views.page_not_found
# handler500 = views.page_error
