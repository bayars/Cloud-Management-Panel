from django.shortcuts import render
from .models import Servers
from .forms import AddServer,RemServer
# Create your views here.

def home(request):
    return render(request,'home.html')


def servers(request):
    s = Servers.objects.all()
    return  render(request,'server.html',{'sv':s})

def addserver(request):
    if request.method == 'POST':
        form = AddServer(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Server added succesfully'
            return render(request,'addserver.html',{'form':form,'msg':msg})
    form = AddServer() 
    msg = 'Add your server'
    return render(request,'addserver.html',{'form':form,'msg':msg})

def removeserver(request):
    if request.method == 'POST':
        form = RemServer(request.POST)
        if form.is_valid():
            a = form.cleaned_data['boxname']
            row = Servers.objects.get(boxname=a)
            row.delete()
            msg = 'Server deleted choose another one'
            form = RemServer()
            return render(request,'removeserver.html',{'form':form,'msg':msg})
    form = RemServer()
    msg ='Choose One'
    return render(request,'removeserver.html',{'form':form,'msg':msg})