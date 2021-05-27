# Puppet for unlimited requests
excec { '/usr/bin/env sed -i s/15/4096/ /etc/default/nginx': }
-> exce { '/usr/bin/env/ service nginx restart': }