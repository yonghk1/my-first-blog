from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^delete/(\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #url(r'^update/(\d+)/$', views.update),

    # url(r'^$', views.user_list, name='user_list'),
    # url(r'^user/(?P<pk>\d+)/$', views.post_detail, name='user_detail'),
    # url(r'^user/new/$', views.post_new, name='user_new'),
    # url(r'^user/(?P<pk>\d+)/edit/$', views.post_edit, name='user_edit'),
]
