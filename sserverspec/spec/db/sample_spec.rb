require 'spec_helper'

print @property[:server_id]

describe command('cat /etc/redhat-release') do
  its(:stdout) { is_expected.to eql("CentOS Linux release 7.3.1611 (Core) \n")}

  its(:stdout) { is_expected.to match(/CentOS Linux release 7.*/)}
end

