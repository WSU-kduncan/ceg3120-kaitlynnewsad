# Part 2 - Setup Load Balancing TODOs
Setup the following and add documentation or screenshots to your README.md file as specified.

1. Create an /etc/hosts OR .ssh/config file on each system that correlates hostnames to private IPs.
    - Description of how file is configured
      Both servers .ssh/config folder. Each proxy would be:
      
        Host webserver1
        HostName 10.0.1.11
        user ubuntu
        IdentityFile /home/ubuntu/ceg3120-aws-vm.pem

        Host webserver2
        HostName 10.0.1.12
        user ubuntu
        IdentityFile /home/ubuntu/ceg3120-aws-vm.pem

2. Document how to SSH in between the systems utilizing their private IPs.
    Use the private IP, username (ubuntu), and the private key called ceg3120-aws-vm.pem.
    To ssh into between the systems examples:
    web server 1: ssh -i ceg3120-aws-vm.pem ubuntu@10.0.1.11
    web server 2: ssh -i ceg3120-aws-vm.pem ubuntu@10.0.1.12


3. HAProxy configuration & documentation requirements
- How to set up a HAProxy load balancer
  - What file(s) where modified & their location
    /etc/haproxy/haproxy
    
  - What configuration(s) were set (if any)
        front proxyfront
        bind 10.0.0.10:80
        default_backend myservers

        back myservers
        balance roundrobin
        server webserver1 10.0.1.11:80
        server webserver2 10.0.1.12:80
 
 
  - How to restart the service after a configuration change
    sudo systemctl restart haproxy
    
  - Resources used (websites)
    https://discourse.haproxy.org/t/question-about-restarting-the-service/4134
    https://upcloud.com/community/tutorials/haproxy-load-balancer-ubuntu/#:~:text=Setting%20up%20HAProxy%20for%20load,cfg%20with%20the%20defining%20settings.


4. Webserver 1 & 2 configuration & documentation requirements
- How set up a webserver
  - What file(s) were modified & their location
    /var/www/html/index.html was modified
    
  - What configuration(s) were set (if any)
     The configurations were set to default default apache2 configurations.
     
  - Where site content files were located (and why)
    The sites are located in the deault location called in /var/www/html/. 
    They are stored because you need to store the index.html is the default for homepage.
 
  - How to restart the service after a configuration change
    sudo systemctl restart apache2
    
  - Resources used (websites)
    https://ubuntu.com/server/docs/web-servers-apache
    
5. From the browser, when connecting to the proxy server, take two screenshots.
  - one screenshot that shows content from "server 1"
    <img width="618" alt="web server 1" src="https://user-images.githubusercontent.com/56359938/158195600-6f66c2f2-425b-4cd3-a02c-48661b78b106.png">


  - one screenshot that shows content from "server 2"
  <img width="849" alt="web server 2" src="https://user-images.githubusercontent.com/56359938/158195639-ae06e23a-c486-41e7-ada7-c809368869f9.png">



