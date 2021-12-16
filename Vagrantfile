# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", path: "./install_docker.sh"
  config.vm.provision "file", source: "./cloud_project", destination: "$HOME/projects/cloud_project"
end
