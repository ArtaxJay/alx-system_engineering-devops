# Prepare the Nginx Server to handle many request at a time without breaking.
# This was by sending 2000 requests, 100 at a tume using ApacheBench.

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
