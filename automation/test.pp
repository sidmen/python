# == Class: to_yaml_test
#
class to_yaml_test (
  $hash = {}
){
$output = $hash.to_yaml
notify {"Output is : \n ${output}": }

file { '/opt/config.yml':
      ensure  => present,
      owner   => 'root',
      group   => 'root',
      mode    => '0644',
      content => "# This file is managed by Puppet. DO NOT EDIT.\n\n ${output}",
      # require => File["${source_files_path}"]
}

}
