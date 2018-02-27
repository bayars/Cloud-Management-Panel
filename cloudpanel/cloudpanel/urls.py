from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
import manager
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','explorer.views.home',name='home'),
    url(r'^servers/$','explorer.views.servers'),
    url(r'^addserver/$','explorer.views.addserver'),
    url(r'^removeserver/$','explorer.views.removeserver'),
    url(r'^manage/(?P<server>[\w]+)/(?P<path>[\w]+)/$','manager.views.filemanager'),
    url(r'^navback/(?P<server>[\w]+)/(?P<path>[\*\w]+)/$','manager.views.navbackward'),
    url(r'^naviforward/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<dir>[\w]+)/$','manager.views.navforward'),
    url(r'^edit/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<file>[\.\w]+)$','manager.views.editdata'),
    url(r'^saveandsend/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<file>[\.\w]+)$','manager.views.senddata'),
    url(r'^upload/(?P<server>[\w]+)/(?P<path>[\*\w]+)$','manager.views.uploadfile'),
    url(r'^delete/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<file>[\.\w]+)$','manager.views.deletefile'),
	#url(r'^servers/$','explorer.views.servers'),
    #url(r'^servers/$','explorer.views.servers'),/\

    
]
 