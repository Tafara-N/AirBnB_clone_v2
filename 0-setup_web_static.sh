#!/usr/bin/env bash
# Setting up web servers for the deployment of web_static project

echo -e "Updating system before set up...\n"
sudo apt-get update ; sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

echo -e "Setting up project structure...\n"

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default


echo -e "Servers set up, restarting Nginx...\n"

sudo service nginx restart

echo -e "Done!\n"
