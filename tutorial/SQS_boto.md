# AWS Simple Queue Service (SQS) using boto
Amazon Simple Queue Service (Amazon SQS) is a message queuing service which is used to send, store, and receive message between software componenents \cite{hid-sp18-402-sqs}. These steps are for seting up environment to use AWS services from python and sample code to work with SQS \cite{hid-sp18-402-sqst} \cite{hid-sp18-402-boto} \cite{hid-sp18-402-botot}.

## Prerequiset
AWS account and access to AWS Management console.

## Create IAM User
To access SQS programatically, we need to do one time setup like createion of IAM user,
get access key id and secret access key
* Log in to the AWs management console
* Select IAM
* Click Users > Add User
* Enetr User Name as Administrator, select access type as AWS Management Console access, select console password
as custom password and enter password in the box. You can also force password rest by checking Require password reset checkbox, in this 
case we are not forcing password change.
* Click Next Permissions button
* Select "Add user to group" on the next screen and click Create Group
* Enter group name as Administrators. Select Job function as filter or enetr AdministratorAccess in search box in front of the filter.
Select AdministratorAccess from the policy names listed.
* Click Create Group button
* Newly created group will be shown selected. Select the newly created group if it is not selected and click on Review button.
* Click Create User on the next screen
* System will provide confirmation of new user creation

## Get Access Key ID and Secret Access Key
Access key id and secret key is required to access AWS SQS through APIs
* In Management console, Navigate to IAM > Users
* Click on newly created user Administrator
* Click Security Credentail tab and then create access key button
* Download access key .csv file and save in secure location

## Setup python
* install python boto library
```
	pip install boto3
``` 
* Install awscli if not installed and set configuration. You will have to provide 
access key and secret key generated in previous step during aws configuration.
```
	pip install awscli
	aws configure
``` 
## Use python to work with SQS
* Create queue
```
	# Get the service resource
	sqs = boto3.resource('sqs')
	queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

``` 
* Send Message
```
	# Get the service resource
	sqs = boto3.resource('sqs')

	# Get the queue
	queue = sqs.get_queue_by_name(QueueName='test')

	# Create a new message	
	response = queue.send_message(MessageBody='Hello World')
```
* Process Message
```
	# Get the service resource
	sqs = boto3.resource('sqs')

	# Get the queue
	queue = sqs.get_queue_by_name(QueueName='test')

	# Process messages by printing out body
	for message in queue.receive_messages():
    		# Print out the body and author (if set)
    		print(message.body)
    		# Let the queue know that the message is processed
    		message.delete()
```

