from django.contrib import admin
from .models import Servers
# Register your models here.


class CloudServers(admin.ModelAdmin):
    list_display = ('__str__','ip')
    
admin.site.register(Servers,CloudServers)