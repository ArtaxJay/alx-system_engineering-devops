# Optimize Nginx server to handle bulky requests successfully

file_line { 'increase_ulimit':
  path  => '/etc/default/nginx',
  line  => 'ULIMIT="-n 4096"',
  match => '^ULIMIT="-n',
  notify => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => 'service nginx restart',
  refreshonly => true,
}
