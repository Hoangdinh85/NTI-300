#!/usr/bin/python
import os
#install python
os.system('yum -y install python-pip')
os.system('pip install virtualenv')
os.system('pip install --upgrade pip')
#make a directory call /opt/django
os.mkdir('/opt/django')
os.chdir('/opt/django')
#install python36#
os.system('yum -y install python36')
os.system('virtualenv -p python36 django')
#os.system('source /opt/django/django/bin/activate && pip install django')
#os.chdir('/opt/django')
os.system('source /opt/django/django/bin/activate && pip install django' + \
           '&& django-admin --version ' + \
           '&& django-admin startproject project1')
#change ownership#
os.system('chown -R hdinh47056 /opt/django')
#os.system('chown -R hdinh47056 project1')
os.system("myip=$(curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//') && sed -i \"s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \[\'$myip\'\]/g\" /opt/django/project1/project1/settings.py")
#start the django server#
os.system('sudo -u hdinh47056 sh -c "source /opt/django/django/bin/activate && python /opt/django/project1/manage.py runserver 0.0.0.0:8000&" ')
