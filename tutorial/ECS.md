# AWS Elastic Container Service

\TODO{No images provided so it is difficult to follow}

Amazon Elastic Container Service (Amazon ECS) is used to deploy Docker containers. Following steps are to run docker container on the ECS through AWS management console referenced and modified as required from Deploy Docekr Container tutorial \cite{hid-sp18-402-ecst}.

## Prerequisite

AWS account and access to AWS Management console.

## Create Task Definition

A task is the blueprint of the application. This tutorial will deploy the default sample web app in the docker container.
* Login to the AWs management console
* Enter task name, container name, an image for the docker container, memory limit, and port mappings
* Click Next Step

## Configure Service

* Configure service by providing service name and the desired number of tasks
* ECS will maintain the number of copies provided in the desired number of tasks
* Check box for load balancing to use application load balancer
* Keep default load balance attributes or change as per the need
* Select service IAM role from available options or create default ecsServiceRole role
* Click Next Step

## Configure Cluster

Task configured in previous steps will run on EC2 instance. This will configure the EC2 cluster.
* Enter cluster name, EC2 instance type, number of instances and key pair
* Configure Security access by configuring known IP address for the access
* Select instance IAM role or create default ecsInstanceRole
* Click on Review and Launch

## Review and Launch Resource

* Review information entered till now
* Edit information as needed
* Click on Review Instance and Run Service
* Next screen shows launch progress. Wait till service is launched. View Service button will be enabled once service is launched.
* Click on View Service once enabled

## Access Deployed Application

* Click Details tab
* Click Load Balancers Under Load Balancing
* Copy DNS Name and enter on the web browser address bar
* You should see web page from app deployed in the docker container

## Clean Up

Release the resource created till now ECS Cluster, EC2 and load balancer
* ECS serice can be release by updating task to 0 and then deleting the service
* In ECS Console, Click on Clusters
* Click Default
* Select service name checkbox and click update
* Change number of tasks to 0
* Click Next on subsequent screens and Update service on the last screen
* Go back to service listing again and select Delete
* Alternatively service can be deleted without updating number of task to 0. In this case delete will change number of task to 0 and then delete the service.
* Follow the on-screen instructions to delete the service. This will release ECS service.
* Log in to EC2 console
* Click on Instance link in the left navigation
* Select the instance
* Select Actions > Instance State > Terminate. This will release EC2 instance.
* Click on Load Balancing > Load Balancer from the left-hand navigation
* Select load balancer
* Select Action > Delete. This will release the load balancer.
