#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
cd /var/www/html
echo "<html><body bgcolor="#0096FF"><h1>This is a WebServer on $(hostname -f) </h1></body></html>" > index.html


