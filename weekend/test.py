import boto3

# Create EC2 client
ec2 = boto3.resource('ec2')

# Launch EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',           # Change as needed
    KeyName='your-key-pair-name'       # Replace with your key pair name
)

print(f"Created EC2 instance with ID: {instances[0].id}")