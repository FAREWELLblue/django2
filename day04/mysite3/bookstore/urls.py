from django.conf.urls import url

from bookstore import views

urlpatterns=[
    url(r'^all_book$',views.all_book,name='all_book'),
    url(r'^update_book/(\d+)',views.update_book),
    url(r'^delete_book/(\d+)',views.delete_book),


]