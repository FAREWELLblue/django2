from django.conf.urls import url
from django.views.decorators.cache import cache_page
from goods import views

urlpatterns=[
    url(r'^/index',cache_page(600,cache='goods')(views.GoodsIndexView.as_view())),
    url(r'^/detail/(?P<sku_id>\d+)$', views.GoodsDetailView.as_view()),
]