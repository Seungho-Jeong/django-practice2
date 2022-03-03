from django.urls import path, re_path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change-password/', views.password_change, name='password_change'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.edit_profile, name='edit_profile'),
    re_path(r'^(?P<username>[\w.@+-]+)/follow/$', views.user_follow, name='user_follow'),
    re_path(r'^(?P<username>[\w.@+-]+)/unfollow/$', views.user_unfollow, name='user_unfollow'),
]
