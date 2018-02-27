from django.shortcuts import render
from explorer.models import Servers
from django.http import HttpResponse
import paramiko
import logging
from .form import fileuploadform
paramiko.util.log_to_file("filename.log")
# Create your views here.

def filemanager(request,server,path):
	s = Servers.objects.get(boxname = server)
    	orginalpath = s.path
    	a = orginalpath.split('/')
    	a = [k for k in a if k]
    	orginalpath = "/".join(a)
	orginalpath = "/"+orginalpath+"/"
	if path == 'new':
		path = orginalpath
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(s.ip,port=s.port,username=s.username,password=s.password)
    	t=paramiko.Transport((s.ip,s.port))
    	t.connect(username=s.username,password=s.password)
    	sftp = paramiko.SFTPClient.from_transport(t)
    	remotefiles = listfiles(path,ssh,server,sftp)
    	remotedirs = listdirs(path,ssh,server,sftp)
    	ssh.close()
    	sftp.close()
    	modpath = path.replace('/','*')
	form = fileuploadform
    	return render(request,'manage.html',{'files':remotefiles,'dirs':remotedirs,'path':path,'orginalpath':orginalpath,'server':server,'modpath':modpath,'form':form})
        
	
	
def listfiles(path,ssh,server,sftp):
	cmd = "cd " + path
	lf = "ls -p "
	stdin,stdout,stderr = ssh.exec_command(cmd + " && " + lf)
	data = stdout.read()
	return data.split()
 	#for i in sftp.listdir():
	#	lstatout=str(sftp.lstat(i)).split()[0]
	#	if 'd'  in lstatout: return sftp.listdir()
#def listfiles(path,ssh,server,sftp):
 #   cmd = "cd "+path
  #  lf = "ls -p | grep -v /"
   # f = open('dumps/' + server + 'traverse.sh','w+')
   # f.write('#!/bin/bash\n')
   # f.close()
   # f = open('dumps/'+ server + 'traverse.sh','a+')
   # f.write(cmd + "\n")
   # f.write(lf)
   # f.close()
   # sftp.put('dumps/' + server +'traverse.sh ','traverse.sh')
   # ssh.exec_command("chmod 777 traverse.sh")
   # stdin,stdout,stderr = ssh.exec_command("./traverse.sh")
   # data = stdout.read()
   # ssh.exec_command("rm -rf traverse.sh")
   # return data.split()

def listdirs(path,ssh,server,sftp):
	cmd = "cd " + path
	ld = "ls -f */ | cut -f1 -d '/'"
	stdin,stdout,stderr = ssh.exec_command(cmd + " && " + ld)
	data = stdout.read()
	return data.split()
	#for i in sftp.listdir():
	#	lstatout = str(sftp.lstat(i)).split()[0]
	#	if 'd' not in lstatout: return sftp.listdir()
    	#cmd = "cd " +path
    	#ld = "ls -f */ | cut -f1 -d '/'"
    	#f = open('dumps/' + server + "traverse.sh",'w+')
    	#f.write('#!/bin/bash\n')
    	#f.close()
    	#f = open('dumps/' + server + 'traverse.sh','a+')
    	#f.write(cmd + "\n")
    	#f.write(ld)
    	#f.close()
    	#sftp.put('dumps/' + server + 'traverse.sh' , 'traverse.sh')
    	#ssh.exec_command("chmod 777 traverse.sh")
    	#stdin, stdout, stderr = ssh.exec_command("./traverse.sh")
    	#data = stdout.read()
    	#ssh.exec_command("rm -rf traverse.sh")
    	#return data.split()

def navforward(request,server,path,dir):
	path = path.replace('*','/')
	path = path + dir + '/'
	return filemanager(request,server,path)


def navbackward(request,server,path):
	a = path.split('*')
	a = [s for s in a if s]
	del a[-1]
	path = "/".join(a)
	path = '/'+path+'/'
	return filemanager(request,server,path)


def editdata(request,server,path,file):
	size = checkfilesize(request,server,path,file)
	if size == True:
		s = Servers.objects.get(boxname = server)
		t = paramiko.Transport((s.ip,s.port))
        	t.connect(username=s.username,password=s.password)
        	sftp = paramiko.SFTPClient.from_transport(t)
		path = path.replace('*','/')
		getfile = path + file
		f1 = open("dumps/"+server+"temp.txt","w+")
		sftp.getfo(getfile,f1)
		f1.close()
		f = open("dumps/"+server+"temp.txt","r+")
		content = f.read()
		return HttpResponse(content,content_type='text/plain')
	elif size == False:
		content = "ErrorSize"
		return HttpResponse(content,content_type='text/plain')
		
def checkfilesize(request,server,path,file):
		path = path.replace('*','/')
		checkfile = path + file
		cmd = "ls -l "+checkfile+" | awk '{print $5}'"
		s = Servers.objects.get(boxname = server)
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(s.ip,port=s.port,username=s.username,password=s.password)
		stdin,stdout,stderr = ssh.exec_command(cmd)
		size = int(stdout.read())
		if size < 1000000:
				return True
		else:
				return False
		
def senddata(request,server,path,file):
		s = Servers.objects.get(boxname=server)
		content = request.GET['content']
		t = paramiko.Transport((s.ip,s.port))
		t.connect(username=s.username,password=s.password)
		sftp= paramiko.SFTPClient.from_transport(t)
		path = path.replace('*','/')
		putfile = path + file
		f1 = open("dumps/"+server + "temp.txt","w+")
		f1.write(content)
		f1.close()
		f = open("dumps/"+ server+ "temp.txt","r+")
		sftp.putfo(f,putfile)
		f.close()
		return HttpResponse("File Updated successfully",content_type='text')
	
def uploadfile(request,server,path):
	if request.method == 'POST':
		f = request.FILES['file']
		fname = request.FILES['file'].name
		fw = open('dumps/'+fname,'w+')
		for chunk in f.chunks():
			fw.write(chunk)
		fw.close()
		f = open('dumps/'+fname,'r+')
		path = path.replace('*','/')
		s = Servers.objects.get(boxname = server)
		t = paramko.Transport((s.ip,s.port))
		t.connect(username=s.username,password=s.password)
		sftp = paramiko.SFTPClient.from_transport(t)
		sftp.put('dumps/'+fname,path+fname)
		sftp.close()
		return filemanager(request,server,path)
	
def deletefile(request,server,path,file):
	path = path.replace('*','/')
	delfile = path + file
	cmd = "rm -rf " + delfile
	s = Servers.objects.get(boxname = server)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(s.ip,port=s.port,username=s.username,password=s.password)
	ssh.exec_command(cmd)
	ssh.close()
	return filemanager(request,server,path)