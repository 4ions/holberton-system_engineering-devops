# install nginx
exec {'/usr/bin/env apt-get -y update': }
exec {'/usr/bin/env apt-get -y install nginx': }
exec {'/usr/bin/env echo "Holberton School" > /var/www/html/index.nginx-debian.html': }
exec {'/usr/bin/env sed -i "/server_name _;/ a\\\terror_page 404 /custom_404.html;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env service nginx start': }