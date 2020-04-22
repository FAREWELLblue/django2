from django.conf.urls import url
from . import views

urlpatterns= {
    #127.0.0.1/v1/carts/<username>
    url(r'^/(?P<username>\w+)$',views.CartsView.as_view())
}