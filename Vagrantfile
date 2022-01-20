# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"

  config.vm.network "forwarded_port", guest: 8080, host: 8123

  config.vm.provision "shell", path: "./install_docker_vagrant.sh"
  config.vm.provision "shell", path: "./install_docker_compose_vagrant.sh"
  config.vm.provision "file", source: "./compose_cloud_project", destination: "$HOME/compose_cloud_project"
  config.vm.provision "file", source: "./nginx", destination: "$HOME/nginx"
  #config.vm.provision "file", source: "./web_app", destination: "$HOME/web_app"
  config.vm.provision "shell", path: "./run_project_vagrant.sh", run: "always"
end
