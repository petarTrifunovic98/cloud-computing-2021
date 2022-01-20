# Petar Trifunović, br. indeksa E2 4/2021
# cloud-computing-2021


# Vagrant
- run "vagrant up" to start the machine
- the "docker-compose up" command runs every time the vm is started or reloaded
- use "localhost:8123" on the host machine to access the nginx server on the guest machine:
    - "localhost:8123" will throw an error, since no method is available on this route
    - "localhost:8123/counter" will access the counters from the two web app containers, using round robin load balancing
    - "localhost:8123/workers" will return an empty array, since no workers were created
- to stop the containers:
    - run "vagrant ssh" in a new terminal
    - "cd ./compose_cloud_project"
    - "docker-compose down"