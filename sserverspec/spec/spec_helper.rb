require 'serverspec'
require 'net/ssh'
require 'yaml'

set :backend, :ssh

if ENV['ASK_SUDO_PASSWORD']
  begin
    require 'highline/import'
  rescue LoadError
    fail "highline is not available. Try installing it."
  end
  set :sudo_password, ask("Enter sudo password: ") { |q| q.echo = false }
else
  set :sudo_password, ENV['SUDO_PASSWORD']
end

properties = YAML.load_file('properties.yml')
longname = ENV['TARGET_HOST']
@property = properties[longname]
host = longname.split('.', 2)[1]
print "Target host is : " + host.to_s + "\n"

options = Net::SSH::Config.for(host)

#options[:user] ||= Etc.getlogin
options[:user]     ||= 'naoshi'
options[:password] ||= 'system'

set :host,        options[:host_name] || host
set :ssh_options, options

# Disable sudo
set :disable_sudo, true

# Set environment variables
# set :env, :LANG => 'C', :LC_MESSAGES => 'C'

# Set PATH
# set :path, '/sbin:/usr/local/sbin:$PATH'
