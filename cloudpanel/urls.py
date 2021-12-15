from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView
import explorer.views
import manager.views
admin.autodiscover()

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^$',explorer.views.home,name='home'),
    path(r'^servers/$', explorer.views.servers),
    path(r'^addserver/$', explorer.views.addserver),
    path(r'^removeserver/$', explorer.views.removeserver),
    path(r'^manage/(?P<server>[\w]+)/(?P<path>[\w]+)/$', manager.views.filemanager),
    path(r'^navback/(?P<server>[\w]+)/(?P<path>[\*\w]+)/$', manager.views.navbackward),
    path(r'^naviforward/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<dir>[\w]+)/$', manager.views.navforward),
    path(r'^edit/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<file>[\.\w]+)$', manager.views.editdata),
    path(r'^saveandsend/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<file>[\.\w]+)$', manager.views.senddata),
    path(r'^upload/(?P<server>[\w]+)/(?P<path>[\*\w]+)$', manager.views.uploadfile),
    path(r'^delete/(?P<server>[\w]+)/(?P<path>[\*\w]+)/(?P<file>[\.\w]+)$', manager.views.deletefile),
	#path(r'^servers/$','explorer.views.servers'),
    #path(r'^servers/$','explorer.views.servers'),/\


]
