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
    config.vm.provider "virtualbox" do |vb|
        vb.gui = true
        vb.memory = "1024"
    end

    config.vm.provider "virtualbox" do |v|
        v.linked_clone = true
    end

    # loop through each env variable to add
    env_vars.each do |env_var_name, env_var_value|
        config.vm.provision "shell", inline: <<-SHELL
            Write-Output "Adding environment variable: #{env_var_name}"
            [Environment]::SetEnvironmentVariable('#{env_var_name}', '#{env_var_value}', 'Machine')
        SHELL
    end

    # config.vm.provision "shell", path: "install_errbot.ps1"

    # config.vm.provision "shell", inline: <<-SHELL
    #     if (!(Get-Command -Name 'choco'))
    #     {
    #         $env:chocolateyUseWindowsCompression = 'true'
    #         iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
    #     }

    #     choco install python -version 3.5.2.20161029 -y
    #     choco install git.install -y

    #     # Leaving test tools out, maybe these will work in Docker instead
    #     # sudo pip -q install coverage
    #     # sudo pip -q install pytest-pep8
    #     # mkdir -p /vagrant/err-data
    #     # mkdir -p /vagrant/err-plugins
    # SHELL

    # config.vm.provision "shell", inline: <<-PYTHON
    #     $env:Path += ";C:\\Program Files\Git\bin\"
    #     python -m pip install --upgrade pip

    #     New-Item -Type Directory -Path 'C:\\errdata' -Force
    #     python -m pip install err
    #     python -m pip install slackclient
    #     python -m pip install git+https://github.com/alvaroaleman/pywinrm.git@bugfix/python3_stderr#egg=pywinrm
    # PYTHON

  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "public_network"
  # config.vm.synced_folder "../data", "/vagrant_data"
end
