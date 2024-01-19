#!/usr/bin/pup
# This mani file will install Flask lib of ver (2.1.0)

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
