from django.db import models

# Create your models here.
class Servers(models.Model):
    boxname = models.CharField(max_length = 15,unique = True)
    ip =models.GenericIPAddressField(protocol='both',unpack_ipv4=False,unique=True)
    port = models.PositiveIntegerField(default = 22)
    username = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)
    path = models.CharField(max_length = 50,default = '/home/username/')
    
    def __str__(self):
        return self.boxname 