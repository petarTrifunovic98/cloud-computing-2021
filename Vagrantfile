# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"

  config.vm.network "forwarded_port", guest: 8080, host: 8123

  #config.vm.provision "shell", path: "./install_docker.sh"
  #config.vm.provision "shell", path: "./install_docker_compose.sh"
  #config.vm.provision "file", source: "./cloud_project", destination: "$HOME/projects/cloud_project"
  #config.vm.provision "file", source: ".", destination: "$HOME/cloud_project"
  config.vm.provision "shell", path: "./run_project_vagrant.sh", run: "always"
end
