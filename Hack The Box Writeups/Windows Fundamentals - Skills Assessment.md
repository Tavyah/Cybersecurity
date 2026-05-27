Skills Assessment - Windows Fundamentals

Introduction:
Inlanefreight recently had an incident where a disgruntled employee in marketing accessed an internally hosted HR share and deleted several confidential files & folders. Thankfully, the IT team had good backups and restored all of the deleted data. There are now concerns that this disgruntled employee was able to access the HR share in the first place. After performing a security assessment, you have found that the IT team may not fully understand how permissions work in Windows. You are conducting training and a demonstration to show the department good security practices with file sharing in a Windows environment as well as viewing services from the command line to check for any potential tampering.

Steps to demonstrate:
1. Creating a shared folder called Company Data

![Creating folder](image.png)
Enabling sharing on the networking via the Advanced Sharing and limiting number of employees to access the shared folder. This is good practice to always set. Setting the limit to 10, however make sure you know how many is needed to access the folder. I am just making an example by setting it to 10.
![Enabling sharing on the network](image-8.png)
![Shared folder](image-2.png)
2. Creating a subfolder called HR inside of the Company Data folder

![Creating a subfolder named HR inside Company Data folder](image-3.png)
3. Creating a user called Jim
    Uncheck: User must change password at logon

![Creating a new user](image-4.png)
![Creating the user Jim](image-5.png)
4. Creating a security group called HR

![Creating a new group](image-6.png)
5. Adding Jim to the HR security group

![Adding Jim to the Security Group](image-7.png)
6. Adding the HR security group to the shared Company Data folder and NTFS permissions list
    Remove the default group that is present
    Share Permissions: Allow Change & Read
    Disable Inheritance before issuing specific NTFS permissions
    NTFS permissions: Modify, Read & Execute, List folder contents, Read, Write

Opening Permissions tab under Advanced Sharing. Here you can see that the default group is "Everyone" and the permission is set to "Read".
![Permissions for Company Data](image-9.png)
Adding HR Security Group to Permissions and setting the share permissions to Allow Change and Read.
![Adding HR Security Group to Permissions for Company Data](image-10.png)
Folders and files inherit the NTFS permissions of their parent folder, this is to save time for administrators, because if you had to set permissions to each folder and file that is created, it would be very time-consuming. However in this case, we want to disable inheritance to make sure we know exactly who has what permissions to the folder. We only want the HR security group and administrator which is us, to have any sort of permission to the Company Data folder.
![Disabling inheritance](image-11.png)
![Removing inheritance](image-12.png)
![Adding HR and setting NTFS permissions](image-14.png)
7. Adding the HR security group to the NTFS permissions list of the HR subfolder
    Remove the default group that is present
    Disable Inheritance before issuing specific NTFS permissions
    NTFS permissions: Modify, Read & Execute, List folder contents, Read, and Write

Setting the NTFS permissions for the HR subfolder aswell.
![Setting the NTFS permissions on the HR subfolder](image-15.png)
8. Using PowerShell to list details about a service

![Listing the Windows Update service](image-16.png)

Questions to answer:

Question 1
What is the name of the group that is present in the Company Data Share Permissions ACL by default?

The Company Data folder's ACL permissions by default is something you will come across at step 6. Remember that the ACL is what you can also consider as the Server Message Block protocol (SMB) permissions list. This ACL list contains access control entires (ACEs) and are made up of users and groups, which you can call security principals. We use these groups and users to manage and track access to shared resources.

The answer is "Everyone".


Question 2
What is the name of the tab that allows you to configure NTFS permissions?

New Technology File System (NTFS) is the default file system for Windows since NT 3.1 and this question was answered during step 6. 

The answer is "Security".

Question 3
What is the name of the service associated with Windows Update?

Using the command Get-Service, you can list out the service for Windows Update and its relevant information, this is done in step 8.

The answer is "wuauserv".

Question 4
List the SID associated with the user account Jim you created.

By using commands Get-LocalUser and Select-Object, you can query out the spesific name Jim and his SID. 

The reason I have "Select-Object Name,SID", the name queried twice is only because I prefer to list out the name in a neat line then the SID. If you remove the Name parameter in the Select-Object, you will only get the SID for that spesific user. It's just a preference to how you like things listed out in cmd.
![Listing SID of Jim](image-17.png)

The answer is "S-1-5-21-2614195641-1726409526-3792725429-1006".

Question 5
List the SID associated with the HR security group you created.

With the command Get-LocalGroups and Select-Object, you can query out the spesific name HR and the groups SID. 
![Listing HR group and it's SID](image-18.png)

The answer is "S-1-5-21-2614195641-1726409526-3792725429-1007".
