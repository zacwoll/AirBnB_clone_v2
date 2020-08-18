# Installs nginx and sets up web_static
exec { 'apt-get -y update' : }
exec { 'apt-get -y install nginx' : }
exec { 'mkdir -p /data/web_static/releases/test /data/web_static/shared' : }
exec { 'echo "Holberton School" > /data/web_static/releases/test/index.html' : }
exec { 'ln -sf /data/web_static/releases/test /data/web_static/current' : }
exec { 'chown -R ubuntu:ubuntu /data' : }
exec { 'grep -q "location /hbnb_static" /etc/nginx/sites-available/default || sed -i "/server_name _;/a \\tlocation /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default' : }
exec { 'service nginx restart' : }
