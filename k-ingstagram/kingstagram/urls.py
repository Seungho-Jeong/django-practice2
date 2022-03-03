from django.urls import path, re_path

from . import views

app_name = 'kingstagram'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/detail/<int:pk>/', views.post_detail, name='post_detail'),
    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page'),
]
