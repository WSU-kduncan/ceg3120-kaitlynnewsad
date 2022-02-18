1. Description:

 Modify Description string to state that this is your template and creates the following
 Example description:
   Duncan CF Template to create a VPC, allow SSH access from trusted networks, and create a single instance with an Elastic IP address

2. Mappings:

Adjust AMI to be the AMI of your choice
This section:
AWSRegionUbuntu: # AMI for Ubuntu server in each supported region
us-east-1:   # N. Virginia
  PV64: NOT_SUPPORTED
  HVM64: ami-07d0cf3af28718ef8
  HVMG2: NOT_SUPPORTED
  
3. Resources:

VPC range to be /24
Subnet range to be /28
Tag each resource with a name - last name, cloudformation, resource: Duncan-CF-VPC

4. Security Group Settings:

Allow SSH for a set of trusted networks including:
Your home / where you usually connect to your instances from
Wright State (addresses starting with 130.108)
Instances within the VPC

5. Instance settings:

Set "Tag" "Name" to "LastName-CF-instance"
Set a private IP in your subnet range
Using the configuration script built into the cf-template
Change hostname
Install git, python3, pip3
Use the "CloudFormation" in the AWS console to test your CloudFormation template.

Do not leave stacks running.
If a stack fails during creation, associated resources will also be deleted (it is an all or nothing creation process)
Once your template creates a stack successfully, you may delete the stack
Extra notes:

Anytime you see !Ref, there is a reference being made to a value defined elsewhere. These are fun to track down.
The configuration script uses some bash syntax.
space \ \ means the command continues on a new line. Very nice for readability
&& && need to go inbetween commands. You will see space && \ && \ in between commands - again, readability
