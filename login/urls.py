from django.conf.urls import url
from . import views

# Added 2016/02/26
from django.contrib.auth.views import login
 
urlpatterns = [

    url(r'^$', login),

    url(r'^logout/$', views.logout_page),


    # If user is not login it will redirect to login page
    url(r'^accounts/login/$', login), 

    url(r'^register/$', views.register),

    url(r'^register/success/$', views.register_success),

    url(r'^home/$', views.home),

]
