# Deploy a Lambda Function, S3 and S3 Event using Ansible #

This Ansible Playbook will deploy a Lambda function in AWS. The Lambda function 
will then be used to run a dummy Python script to move files in the associated 
S3 bucket. This code also provides a handy clean-up script.

## Prerequisites ##

You will need the following to use this script:
- Ansible
- An AWS Account 

## Setup the Lambda Python Script ##

Enter the bucket name in python script.

1. Open move_s3_files.py
2. Replace "Enter-name-of-your-bucket" with proper name of your bucket.

## Setup and Run the Ansible Deploy Script ##

To deploy the s3 bucket and lambda function on AWS.

1. Open deploy_lambda.yaml
2. Edit the Vars section with proper values.
3. To deploy and create lambda execute the below commands.

```
ansible-playbook deploy.yaml
```

## Setup and Run the Ansible Destroy Script ##

To destroy the s3 bucket and lambda function on AWS.

1. open destroy.yaml
2. Edit the Vars section with proper values.
3. Now to destroy aws resources execute the below commands.

```
ansible-playbook destroy.yaml
```

## Want to connect?

Feel free to contact me on [Twitter](https://twitter.com/OnlineAnto), [DEV Community](https://dev.to/antoonline/) or [LinkedIn](https://www.linkedin.com/in/anto-online) if you have any questions or suggestions.

Or just visit my [website](https://anto.online) to see what I do.
