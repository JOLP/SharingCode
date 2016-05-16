"""hackIDE_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

# admin을 불러오고 hackIDE.urls 에 설정된 url들을 불러온다.

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('hackIDE.urls')),
    # Added 2016/02/22 By yunhongseog
    # url(r'^', include('login.urls')),
    url(r'^', include('home.urls')),
    url(r'^', include('alpha.urls')),
]
