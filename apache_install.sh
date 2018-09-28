[hdinh47056@apache ~]$ sudo su (become root)
yum install httpd  (To install httpd) 
systemctl enable httpd (Enable httpd)
systemctl status httpd (check status)
systemctl start httpd  (start httpd)
yum -y install mod_ssl
systemctl restart httpd
