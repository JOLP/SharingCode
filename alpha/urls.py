from django.conf.urls import url

from . import views



urlpatterns = [

    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^chatroom/$', views.Chatroom, name='chatroom'),
    url(r'^home/$', views.Home, name='home'),

    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),

    url(r'^register/$', views.register, name='register'),

    url(r'^register/success/$', views.register_success, name='register_success'),
]