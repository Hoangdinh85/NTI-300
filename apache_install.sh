yum install httpd
systemctl enable httpd
systemctl enable status httpd
systemctl status httpd
systemctl start httpd
yum -y install mod_ssl
systemctl restart httpd
