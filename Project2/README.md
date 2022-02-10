# Part 1 - Build a VPC

1. Create a VPC
    - Specify a /24 private IP address range
      - 10.0.0.0/24
![Screenshot 2022-02-09 142617](https://user-images.githubusercontent.com/56359938/153285381-aa9dea90-9239-4c9d-ac12-8d47817a8672.png)

2. Create a subnet
    - Specify a /28 private IP address range
    - Attach it to your VPC
        - 10.0.0.0/28
 ![Screenshot 2022-02-09 142748](https://user-images.githubusercontent.com/56359938/153285443-282ee7f9-6bc9-439a-aaaa-f545d197efcf.png)

3. Create an internet gateway
    - Attach it to your VPC
    ![Screenshot 2022-02-09 143044](https://user-images.githubusercontent.com/56359938/153285598-bd14e61d-d75d-4ea7-8d33-8e06500eb33e.png)


4. Create a route table
    - Attach it to your VPC
    - Associate it with your subnet
    - Add a routing table rule that sends traffic to all destinations to your internet gateway
 ![Screenshot 2022-02-09 143851](https://user-images.githubusercontent.com/56359938/153285644-96dd84f9-8b64-4606-a339-c7b19c261fa8.png)


5. Create a security group
    - Allow SSH for a set of trusted networks including:
      - Your home / where you usually connect to your instances from
      - Wright State (addresses starting with 130.108)
      - Instances within the VPC
![Screenshot 2022-02-09 144434](https://user-images.githubusercontent.com/56359938/153285683-1acbd0c0-4ae9-408f-bf96-74cd7a831c22.png)
- Inbound Rules 
![Screenshot 2022-02-10 104212](https://user-images.githubusercontent.com/56359938/153444544-2420c90f-585e-4403-ae8b-a9b311773dfb.png)


Note: Did not create a key pair used run I had already created one called ceg3120-aws-vm.pem.

# Part 2 
- EC2 instances
1. Create a new instance. 
    - AMI selected
    - Instance type selected
   
 I clicked on lanuch instances on the EC2 dashboard. I then choose Ubuntu Server 20.04 LTS (HVM), SSD Volume Type (64 bit x86) 
  and then choose t2.micro on the next page.

2. Attach the instance to your VPC. As discussed there are different pathways to doing this. Say how you did it.

    To attach the instance to the VPC on tye next page it shows network details. Under the network I attached the Newsad-VPC to the instance.
    This also caused the subnet to be attached to the instance now.
    
![Screenshot 2022-02-09 151856](https://user-images.githubusercontent.com/56359938/153286694-c9a34e0b-7f29-40cb-b3cf-42cd2b36bfeb.png)

3. Determine whether a Public IPv4 address will be auto-assigned to the instance. Justify your choice to do so (or not do so)

   The subnet diables an auto IP address to be assinged. We have to use a Elastic IP which allows us to remmap the address to other 
   instance in the VPC. 
   
4. Attach a volume to your instance. As discussed there are different pathways to doing this. Say how you did it.

    In the next step of creating the instance I had to select a volum to add. I stuck with the deafult and did SSD (gp2).

5. Tag your instance with a "Name" of "YOURLASTNAME-instance". Say how you did it.

    The next step showed tagging the instance I choose the name Newsad-instance for both the value and name. 

6. Associate your security group, "YOURLASTNAME-sg" to your instance. Say how you did it.

    In the next page I clicked on existing secuirty group and choose the ones I created called Newsad-sg.

7. Reserve an Elastic IP address. Tag it with "YOURLASTNAME-EIP". Associate the Elastic IP with your instance. Say how you did it.

   Under Network Settings on the side of the page clicked on Elastic IP. Then clicked on Allocate Elastic IP address and added
    a tag to this IP called Newsad-EPI. Then I clicked on Action then Assoacite Elastic IP and associated the this IP to the instance we created. 

8. Create a screenshot your instance details and add it to your project write up.
![Screenshot 2022-02-10 085620](https://user-images.githubusercontent.com/56359938/153423101-eb081197-8c24-43ac-b440-5e6b9e3b8fb9.png)


9. ssh in to your instance. Change the hostname to "YOURLASTNAME-AMI" where AMI is some version of the AMI you chose. Say how you did it.
    Used the command ssh -i /home/knewsad/ceg3120-aws-vm.pem ubuntu@54.156.184.132.
    Change host name by typing sudo hostnamectl set-hostname Newsad-UbuntuAMI
    ![Screenshot 2022-02-10 104825](https://user-images.githubusercontent.com/56359938/153444818-138ea12a-1988-4785-9257-0466e56273a0.png)

  
10. Create a screenshot your ssh connection to your instance and add it to your project write up - make sure it shows your new hostname.
![Screenshot 2022-02-10 104740](https://user-images.githubusercontent.com/56359938/153444319-29c7315b-90ec-4de4-bbbc-ff1edb4b96c1.png)

Note: You may delete all created resources once done to save monies. No really, trash it - especially the instance and disassociate and release the elastic ip

