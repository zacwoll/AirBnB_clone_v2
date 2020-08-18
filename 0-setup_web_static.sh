#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
grep -q 'location /hbnb_static' /etc/nginx/sites-available/default || sed -i '/server_name _;/a \\tlocation /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
service nginx restart
