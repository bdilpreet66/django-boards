from django.urls import path,re_path
from . import views

#urls start here

app_name = 'boards'

urlpatterns = [
    path('',views.BoardListView.as_view(),name='home'),
    re_path(r'^boards/(?P<pk>\d+)/$',views.TopicListView.as_view(), name = 'board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$',views.NewTopic, name = 'new_topic'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.ReplyTopic, name='reply_topic'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',views.PostUpdateView.as_view(), name='edit_post'),
]
