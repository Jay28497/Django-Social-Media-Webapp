from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('follow', views.follow, name='follow'),
    path('unfollow', views.unfollow, name='unfollow'),
    path('post', views.post, name='post'),
    path('add_comment', views.add_comment, name='add_comment'),
    path('add_subcomment', views.add_subcomment, name='add_subcomment'),
]
