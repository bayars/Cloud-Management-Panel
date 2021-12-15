from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView
import explorer.views
import manager.views
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',explorer.views.home,name='home'),
    path('servers/', explorer.views.servers),
    path('addserver/', explorer.views.addserver),
    path('removeserver/', explorer.views.removeserver),
    path('manage/(?P<server>[\w]+)/(?P<path>[\w]+)/$', manager.views.filemanager),
    path('navback/(?P<server>[\w]+)/(?P<path>[\*\w]+)/$', manager.views.navbackward),
    path('naviforward/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<dir>[\w]+)/$', manager.views.navforward),
    path('edit/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<file>[\.\w]+)$', manager.views.editdata),
    path('saveandsend/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<file>[\.\w]+)$', manager.views.senddata),
    path('upload/(?P<server>[\w]+)/(?P<path>[\*\w]+)$', manager.views.uploadfile),
    path('delete/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<file>[\.\w]+)$', manager.views.deletefile),
	#explorer.views.home  path(r'^servers/$','explorer.views.servers'),
    #path(r'^servers/$','explorer.views.servers'),/\


]
