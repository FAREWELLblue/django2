from django.conf.urls import url

from user import views

urlpatterns=[
    url(r'^detail/(\d+)',views.user_detail),
    url(r'^update$',views.user_update),
]