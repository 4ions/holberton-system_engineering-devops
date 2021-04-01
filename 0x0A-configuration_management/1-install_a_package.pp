# Using Puppet, install puppet-line
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}