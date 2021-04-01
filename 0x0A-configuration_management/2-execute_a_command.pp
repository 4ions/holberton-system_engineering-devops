# Kills a process
exec {'pkill':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}