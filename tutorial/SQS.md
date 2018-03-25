# AWS Simple Queue Service (SQS)
Amazon Simple Queue Service (Amazon SQS) is a message queuing service which is used to send, store, and receive message between software componenents. This tutorial is to demonstrate on how to use AWS SQS using management console.

## Prerequiset
AWS account and access to AWS Management console.

## Create Queue
* Log in to the AWs management console
* Select SQS
* Click Get Started
* Enetr Queue Name and queue type. We have selected queue type as FIFO.
* Click Configure Queue button to set queue attributes
* Click Create Queue to create the queue. Queue created will be visible on the console.

## Add Permission
Add permission to queue for accessibility
* Select created queue > Queue Actions > Add a Permission
* We will add permission for everybody to get the queue's url
* Select Effect as Allow, Principal as Everybody, GetQueueUrl from Actions
* Click on Add Permission
* Newly added permisson can be veiwed on Permissions tab

## Send Message
Send message to queue
* Select queue from the listing
* Click Queue Actions > Send a Message
* Enter message body text, message group id and message duplication id
* Click on Send Message to submit message to the queue
* Confirmation message is displayed
* Click close to close confirmation message
