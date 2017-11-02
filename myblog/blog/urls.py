from django.conf.urls import url
from . import views
from django.contrib.auth import views as viewse

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/upvote/$', views.post_upvote, name='post_upvote'),
    url(r'^post/(?P<pk>\d+)/downvote/$', views.post_downvote, name='post_downvote'),
    url(r'^post/(?P<pk>\d+)/reset/$', views.reset_upvotes_and_downvotes, name='post_reset'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^accounts/logout/$', viewse.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    #url(r'^accounts/login/$', views.login, name='login'),
]
