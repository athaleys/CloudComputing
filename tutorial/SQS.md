# AWS Simple Queue Service (SQS)
Amazon Simple Queue Service (Amazon SQS) is a message queuing service which is used to send, store, and receive message between software componenents \cite{hid-sp18-402-sqs}. 

## SQS using AWS Console
These steps are for seting up the queue, sending/receieving message and deletion of queue using management console \cite{hid-sp18-402-sqst}.

### Prerequiset
AWS account and access to AWS Management console.

### Create Queue
* Log in to the AWs management console
* Select SQS
* Click Get Started
* Enetr Queue Name and queue type. We have selected queue type as FIFO.
* Click Configure Queue button to set queue attributes
* Click Create Queue to create the queue. Queue created will be visible on the console.

### Add Permission
Add permission to queue for accessibility
* Select created queue > Queue Actions > Add a Permission
* We will add permission for everybody to get the queue's url
* Select Effect as Allow, Principal as Everybody, GetQueueUrl from Actions
* Click on Add Permission
* Newly added permisson can be veiwed on Permissions tab

### Send Message
Send message to queue
* Select queue from the listing
* Click Queue Actions > Send a Message
* Enter message body text, message group id and message duplication id
* Click on Send Message to submit message to the queue
* Confirmation message is displayed
* Click close to close confirmation message

### Receive Message
Read message from the queue
* Select queue from the listing
* Click Queue Actions > View/Delete Message
* Click Start Polling for Messages to poll the message
* Message posted in previous step sould be visible

### Delete Message
Delete message from the queue
* Follow steps in previous step to view the message
* Select delete checkbox and click on the Delete Message button
* Click Yes on the confirmation box to permanently delete the message

### Purging and Deleting Queue
Purg action will delete all the messages present in the queue. Delete queue option will delete the queue and will not be available for the further useage.
* To purg, select queue and click on Queue Actions > Purge Queue
* Select Yes on the confirmation box to purege all messages present in the queue
* Click Ok on the next information box
* To delete the queue, Select queue and click on Queue Actions > Delete Queue
* Click Yes on the confirmation message to delete the the queue

## AWS SQS using boto
These steps are for seting up environment to use AWS services from python and sample code to work with SQS \cite{hid-sp18-402-sqst} \cite{hid-sp18-402-boto} \cite{hid-sp18-402-botot}.

### Prerequiset

AWS account and access to AWS Management console.

### Create IAM User

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

### Get Access Key ID and Secret Access Key

Access key id and secret key is required to access AWS SQS through APIs
* In Management console, Navigate to IAM > Users
* Click on newly created user Administrator
* Click Security Credentail tab and then create access key button
* Download access key .csv file and save in secure location

### Setup python

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
### Use python to work with SQS

Create queue
\TODO{use full sentences. To create a queue we use the following code}
```
# Get the service resource
sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='myQueue', Attributes={'DelaySeconds': '5'})

``` 

Send Message
```
# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='myQueue')

# Create a new message	
response = queue.send_message(MessageBody='Hello World')
```

Process Message
```
# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='myQueue')

# Process messages by printing out body
for message in queue.receive_messages():
    	# Print out the body and author (if set)
    	print(message.body)
    	# Let the queue know that the message is processed
    	message.delete()
```

