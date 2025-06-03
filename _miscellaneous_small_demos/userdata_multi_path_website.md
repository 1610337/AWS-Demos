Simple User Data to host a multi-path website (for Amazon Linux 2)

``` bash
#!/bin/bash

# Update and install Apache HTTP Server
yum update -y
yum install httpd -y

# Start and enable Apache
service httpd start
chkconfig httpd on

# Go to the web server root directory
cd /var/www/html

# Create directories
mkdir -p path1 path2 path3

# Create the HTML files
echo "<html><body bgcolor=\"orange\"><h1>This is WebServer 01 on $(hostname -f) - STAGE</h1></body></html>" > path1/index.html
echo "<html><body bgcolor=\"lightblue\"><h1>This is WebServer 01 on $(hostname -f) - PROD</h1></body></html>" > path2/index.html
echo "<html><body bgcolor=\"lightgreen\"><h1>This is WebServer 01 on $(hostname -f) - STABLE</h1></body></html>" > path3/index.html
```
