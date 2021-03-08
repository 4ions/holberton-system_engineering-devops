# Web infrastructure design

In the design of web servers, there are many factors that categorize the level of the server, whether they have a simple and unprotected infrastructure, to web servers that have different systems for failure detection and data care, in this repository will observe different types of infrastructure designs web servers

## File Description

In each file within this repository, there is a link to an image that contains a design of a web server infrastructure.

## 0-simple_web_stack

A whiteboard on a web server infrastructure hosting the website www.foobar.com

This containt:
* 1 server
* 1 web server (Nginx)
* 1 application server
* 1 application files (your code base)
* 1 database (MySQL)
* 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

## 1-distributed_web_infrastructure

A whiteboard on a three servers web server infrastructure hosting the website www.foobar.com

This add:
* 2 physical servers
* 1 web server (Nginx)
* 1 application server
* 1 load-balancer (HAproxy)
* 1 application files (your code base)
* 1 database (MySQL)

## 2-secured_and_monitored_web_infrastructure

Design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

This add:
* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients (data collector for Sumologic or other monitoring services)
