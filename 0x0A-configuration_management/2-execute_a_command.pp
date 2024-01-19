# This mani file will kill the process started by killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
