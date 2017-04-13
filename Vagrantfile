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
    config.vm.define "errbot" do |errbot|
        errbot.vm.box = "MattHodge/Windows2016-WMF5-NOCM"
        errbot.vm.hostname = "errbot"
        errbot.vm.network "private_network", ip: "172.28.128.100"
        errbot.vm.network "forwarded_port", guest: 3389, host: 23339
        errbot.vm.provider "virtualbox" do |vb|
            vb.linked_clone = true
            vb.memory = 2048
            vb.cpus = 1
            vb.gui = true
            vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
            vb.customize ["modifyvm", :id, "--draganddrop", "bidirectional"]
        end

        # remove default vagrant folder
        errbot.vm.synced_folder ".", "/vagrant", disabled: true

        # share the errbot name
        errbot.vm.synced_folder ".", "/errbot"

        # loop through each env variable to add
        env_vars.each do |env_var_name, env_var_value|
            errbot.vm.provision "shell", inline: <<-SHELL
                Write-Output "Adding environment variable: #{env_var_name}"
                [Environment]::SetEnvironmentVariable('#{env_var_name}', '#{env_var_value}', 'Machine')
            SHELL
        end

        errbot.vm.provision "shell", path: "provision/disable_winupdates.ps1"
        errbot.vm.provision "shell", path: "provision/install_errbot.ps1"
    end

    config.vm.define "win2016core" do |win2016core|
        win2016core.vm.box = "MattHodge/Windows2016StdCore-WMF5-NOCM"
        win2016core.vm.hostname = "win2016core"
        win2016core.vm.network "private_network", ip: "172.28.128.101"
        win2016core.vm.network "forwarded_port", guest: 80, host: 8080
        win2016core.vm.network "forwarded_port", guest: 3389, host: 33339
        win2016core.vm.provider "virtualbox" do |vb|
            vb.linked_clone = true
            vb.memory = 1024
            vb.cpus = 1
            vb.gui = true
            vb.customize ["modifyvm", :id, "--clipboard", "bidirectional"]
        end

        # remove default vagrant folder
        win2016core.vm.synced_folder ".", "/vagrant", disabled: true

        win2016core.vm.provision "shell", path: "provision/disable_winupdates.ps1"
    end
end



# config.vm.network "forwarded_port", guest: 80, host: 8080
# config.vm.network "private_network", ip: "192.168.33.10"
# config.vm.network "public_network"
# config.vm.synced_folder "../data", "/vagrant_data"
