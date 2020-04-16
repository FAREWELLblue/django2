from django.conf.urls import url

from user import views

urlpatterns={
    url(r'^reg$',views.reg_view),
    url(r'^login$',views.login_view),
}