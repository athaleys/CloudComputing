# AWS Container Service
Amazon Elastic Container Service (Amazon ECS) is used to deploy docker containers. This tutorial is to run docker container on the ECS.

## Prerequiset
AWS account and access to AWS Management console.

## Create Task Definition
* Log in to the AWs management console
* Enter taske name, container name, image for the docker container, memory limit and port mappings
* Click Next Step

## Configure Service
* Configure service by providing service name and desired number of tasks
* ECS will maintain number of copies provided in desired number of tasks
* Check box for load balancing to use application load balancer
* Keep default load balance attributes or change as per the need

## Configure Cluster
