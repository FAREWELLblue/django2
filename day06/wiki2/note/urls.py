from django.conf.urls import url

from note import views

urlpatterns=[
    url(r'^add$',views.add_view)
]