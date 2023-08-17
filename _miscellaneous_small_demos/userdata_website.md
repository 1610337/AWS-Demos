Simple User Data to host a website (for Amazon Linux 2)

``` bash
#!/bin/bash
yum update -y
yum install httpd -y
service httpd start
chkconfig httpd on
cd /var/www/html
echo "<html><body bgcolor="orange"><h1>This is WebServer 01 on $(hostname -f) </h1></body></html>" > index.html
```