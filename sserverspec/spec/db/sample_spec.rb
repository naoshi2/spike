require 'spec_helper'

print @property[:roles]

describe command('cat /etc/redhat-release') do
  its(:stdout) { is_expected.to eql("CentOS Linux release 7.3.1611 (Core) \n")}

  # Success
  its(:stdout) { is_expected.to match(/CentOS Linux release [6|7].*/)}

  # Fail
  #its(:stdout) { is_expected.to match(/CentOS Linux release [5|6].*/)}
end

