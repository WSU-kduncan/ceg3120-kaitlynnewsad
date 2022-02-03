# Part 1 - Build a VPC

1. Create a VPC
- Specify a /24 private IP address range

2. Create a subnet
- Specify a /28 private IP address range
- Attach it to your VPC
3. Create an internet gateway
- Attach it to your VPC
4. Create a route table
- Attach it to your VPC
- Associate it with your subnet
- Add a routing table rule that sends traffic to all destinations to your internet gateway

5. Create a security group
- Allow SSH for a set of trusted networks including:
  - Your home / where you usually connect to your instances from
  - Wright State (addresses starting with 130.108)
  - Instances within the VPC

# Part 2 - EC2 instances
1. Create a new instance. 
- AMI selected
- Instance type selected

2. Attach the instance to your VPC. As discussed there are different pathways to doing this. Say how you did it.

3. Determine whether a Public IPv4 address will be auto-assigned to the instance. Justify your choice to do so (or not do so)

4. Attach a volume to your instance. As discussed there are different pathways to doing this. Say how you did it.

5. Tag your instance with a "Name" of "YOURLASTNAME-instance". Say how you did it.

6. Associate your security group, "YOURLASTNAME-sg" to your instance. Say how you did it.

7. Reserve an Elastic IP address. Tag it with "YOURLASTNAME-EIP". Associate the Elastic IP with your instance. Say how you did it.

8. Create a screenshot your instance details and add it to your project write up.

9. ssh in to your instance. Change the hostname to "YOURLASTNAME-AMI" where AMI is some version of the AMI you chose. Say how you did it.

10. Create a screenshot your ssh connection to your instance and add it to your project write up - make sure it shows your new hostname.

Note: You may delete all created resources once done to save monies. No really, trash it - especially the instance and disassociate and release the elastic ip

