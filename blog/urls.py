import views
from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$', views.post_list),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit_post$', views.edit_post),
]
