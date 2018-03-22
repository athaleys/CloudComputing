# Swagger Codegen Assignment: AWS VM
  
## Usage

* This service provides capability to create, get and list VMs

* It uses python 2 and MongodDB as a technology

* Post operation is used to create VM in database and get operations
  are used for getting vms from the database.

* 3 operations are provided as 

  * ```/vm``` -- post to create VM
  
  * ```/vms``` -- lists all VMs present in the database
  
  * ```/vms/{vmId}``` -- list VM by VMID


## Instructions for docker installation

* Create and Start docker container using make command. It uses docker compose to launch swagger server and
  MongoDB server in the same container. You will need Docker and Docer Compose installed. Instructions to 
  install docker compose can be found at https://docs.docker.com/compose/install/
  
  * ```make docker-start```

* Test the service using following curl commands
  
   * ```make test```
  
* Stop the service using following commands
  
  * ```make docker-stop```

	
## Instructions for ubuntu without docker

* you should be running this program in python 2 environment.

* you should have default-jre installed.

* you should have mongoDB installed.

* git clone the project.

* change the directory to swagger folder

* create the swagger server with following command
  
  * ```make service```

* run the swagger server with following command
  
  * ```make start```

* start mongodb with following command
  
  * ```make startdb```

* test the program using following command
  
  * ```make test```

* stop the service using following command
  
  * ```make stop```

* clean the server and client codes using following command
  
  * ```make clean```


