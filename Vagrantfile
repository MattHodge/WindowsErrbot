# -*- mode: ruby -*-
# vi: set ft=ruby :

# allows keeping api key out of repo
require 'yaml'

current_dir = File.dirname(File.expand_path(__FILE__))
env_var_file = YAML.load_file("#{current_dir}/.env.yml")
env_vars = env_var_file['configs']

# set a default provider
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'virtualbox'

Vagrant.configure("2") do |config|
    config.vm.box = "MattHodge/Windows2016-WMF5-NOCM"
    #config.vm.box = "MattHodge/Windows2016StdCore-WMF5-NOCM"
    config.vm.provider "virtualbox" do |vb|
        vb.gui = true
        vb.memory = "1024"
    end

    config.vm.provider "virtualbox" do |v|
        v.linked_clone = true
    end

    # remove default vagrant folder
    config.vm.synced_folder ".", "/vagrant", disabled: true

    # share the errbot name
    config.vm.synced_folder ".", "/errbot"

    # loop through each env variable to add
    env_vars.each do |env_var_name, env_var_value|
        config.vm.provision "shell", inline: <<-SHELL
            Write-Output "Adding environment variable: #{env_var_name}"
            [Environment]::SetEnvironmentVariable('#{env_var_name}', '#{env_var_value}', 'Machine')
        SHELL
    end

    config.vm.provision "shell", path: "install_errbot.ps1"

  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "public_network"
  # config.vm.synced_folder "../data", "/vagrant_data"
end
