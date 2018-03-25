# AWS Simple Queue Service (SQS)
Amazon Simple Queue Service (Amazon SQS) is a message queuing service which is used to send, store, and receive message between software componenents. This section is to demonstrate how to use AWS SQS using management console.

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

## Receive Message
Read message from the queue
* Select queue from the listing
* Click Queue Actions > View/Delete Message
* Click Start Polling for Messages to poll the message
* Message posted in previous step sould be visible

## Delete Message
Delete message from the queue
* Follow steps in previous step to view the message
* Select delete checkbox and click on the Delete Message button
* Click Yes on the confirmation box to permanently delete the message

## Purging and Deleting Queue
Purg action will delete all the messages present in the queue. Delete queue option will delete the queue and will not be available for the further useage.
* To purg, select queue and click on Queue Actions > Purge Queue
* Select Yes on the confirmation box to purege all messages present in the queue
* Click Ok on the next information box
* To delete the queue, Select queue and click on Queue Actions > Delete Queue
* Click Yes on the confirmation message to delete the the queue
