from django.conf.urls import patterns, include, url
from sb import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
        
    url(r'^$', views.home),
    url(r'^show_write_form/$', views.show_write_form),   
    url(r'^DoWriteBoard/$', views.DoWriteBoard),
    url(r'^viewWork/$', views.viewWork),
    url(r'^listSpecificPageWork/$', views.listSpecificPageWork),
    url(r'^listSpecificPageWork_to_update/$', views.listSpecificPageWork_to_update),
    url(r'^updateBoard/$', views.updateBoard),       
    url(r'^DeleteSpecificRow/$', views.DeleteSpecificRow),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^searchWithSubject/$', views.searchWithSubject),
    url(r'^listSearchedSpecificPageWork/$', views.listSearchedSpecificPageWork),
    
    
    
)
