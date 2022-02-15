# set up the default terminal
ENV["TERM"]="linux"

# set minimum version for Vagrant
Vagrant.require_version ">= 2.2.10"
Vagrant.configure("2") do |config|
  # Set the image for the vagrant box
  config.vm.box = "ubuntu/focal64"
  # Set the image version
  config.vm.box_version = "20220208.0.0"

  config.vm.provision "shell",
    inline: "curl -sfL https://get.k3s.io | sh -"

  config.vm.provision "shell",
    inline: "apt-get install bash-completion -y"

  config.vm.provision "shell",
    inline: "echo 'source <(kubectl completion bash)' >>~/.bashrc && echo 'source /usr/share/bash-completion/bash_completion' >>~/.bashrc"

  config.vm.provision "shell",
    inline: "kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl > /dev/null"

  # Forward the ports from the guest VM to the local host machine
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 6111, host: 6111
  config.vm.network "forwarded_port", guest: 6112, host: 6112
  config.vm.network "forwarded_port", guest: 30007, host: 30007
  config.vm.network "forwarded_port", guest: 30008, host: 30008

  # Set the static IP for the vagrant box
  config.vm.network "private_network", ip: "192.168.56.1"
  
  # Configure the parameters for VirtualBox provider
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "3072"
    vb.cpus = 4
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
  end
end
