from django.conf.urls import url

from user import views

urlpatterns=[
    # http://127.0.0.1:8000/v1/users
    url(r'^$',views.users),
    url(r'^/activation$',views.active_view),
    url(r'^/(?P<username>\w+)/address$',views.AddressView.as_view()),

    #微博相关
    url(r'^/weibo/authorization$',views.oauth_url_view),
    url(r'^/weibo/users$',views.OauthWeiboView.as_view())
]