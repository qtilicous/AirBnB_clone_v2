#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static.

# Install Nginx if not already installed
apt-get update
apt-get -y install nginx

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
<head>
</head>
<body>
Holberton School
</body>
</html>" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content of /data/web_static/current/
# to hbnb_static
sed -i '/server_name _;/a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
