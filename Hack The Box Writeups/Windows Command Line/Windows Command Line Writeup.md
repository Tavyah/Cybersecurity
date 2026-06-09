# Windows Command Line

## Command Prompt Basics

Insecure and not recommended:
- Telnet

Better optionals:
- Secure Shell (SSH) 
- PsExec
- WinRM
- RDP

### Case study: Windows Recovery
In the event of a user lockout or some technical issue preventing/ inhibiting regular use of the machine, booting from a Windows installation disc gives us the option to boot to Repair Mode. From here, the user is provided access to a Command Prompt, allowing for command-line-based troubleshooting of the device.

Accessing the Command Prompt via Recovery Mode

While useful, this also poses a potential risk. For example, on this Windows 7 machine, we can use the recovery Command Prompt to tamper with the filesystem. Specifically, replacing the Sticky Keys (sethc.exe) binary with another copy of cmd.exe

Once the machine is rebooted, we can press Shift five times on the Windows login screen to invoke Sticky Keys. Since the executable has been overwritten, what we get instead is another Command Prompt - this time with NT AUTHORITY\SYSTEM permissions. We have bypassed any authentication and now have access to the machine as the super user.


### Question 1
In what directory can the cmd executable be found? (just the folder name as answer)

First we will connect to the target machine by using the following command: ssh htb-student@{IP_ADDRESS}

As you open up the session, you will notice a path in the top of the command line console.
![Path on top of console](image-19.png)

The answer is "system32".

## Getting Help

### Commands:
help
help {COMMAND}
{COMMAND} /?
cls

Command history can be looked at by moving keys up and down, page up, page down and also the command "doskey /history". And if working on a physical Windows host, you can use the function key to interact with session history.

Interrupting commands use Control + C

F3	Will retype the entire previous entry to our prompt.
F5	Pressing F5 multiple times will allow you to cycle through previous commands.
F7	Opens an interactive list of previous commands.
F9	Enters a command to our prompt based on the number specified. The number corresponds to the commands place in our history.


### Question 1
If I wanted to view the help documentation for 'ipconfig', what command and/or modifier would I use? (full command string)

The answer is "ipconfig /?".

### Question 2
What CLI equivalent "Help utility" exists on Linux hosts? (one word)

The answer is "man".

### Question 3
Which CMD hotkey will open an interactive list of the previous commands we have ran?

The answer is "F7".

## System Navigation  
Absolute path - considered the absolute path when it follows the complete structure of the file system starting from the root directory
Example: C:\Users\htb\Downloads

Relative path - using our working directory as the starting point to reference directories either above it or below it in the file system hierarchy.
Example: cd .\Downloads - if your current working directory is C:\Users\htb and we want to change to a directory below our current directory

Move up hierarchy use cd ..\, each ..\ represents a directory, meaning u can be in the Downloads folder and move up to the C folder by simply using the following command: cd ..\..\..\


### Commands:
dir - listing of the directory we are currently working in
cd - our current working directory
chdir
tree - listing the file structure
tree /F - listing the file structure with files and directory

### Interesting Directories
#### Name:	Location:	Description:

%SYSTEMROOT%\Temp	C:\Windows\Temp	    Global directory containing temporary system files accessible to all users on the system. All users, regardless of authority, are provided full read, write, and execute permissions in this directory. Useful for dropping files as a low-privilege user on the system.

%TEMP%	    C:\Users\<user>\AppData\Local\Temp	    Local directory containing a user's temporary files accessible only to the user account that it is attached to. Provides full ownership to the user that owns this folder. Useful when the attacker gains control of a local/domain joined user account.

%PUBLIC%	C:\Users\Public	    Publicly accessible directory allowing any interactive logon account full access to read, write, modify, execute, etc., files and subfolders within the directory. Alternative to the global Windows Temp Directory as it's less likely to be monitored for suspicious activity.

%ProgramFiles%	    C:\Program Files	    folder containing all 64-bit applications installed on the system. Useful for seeing what kind of applications are installed on the target system.

%ProgramFiles(x86)%	    C:\Program Files (x86)	    Folder containing all 32-bit applications installed on the system. Useful for seeing what kind of applications are installed on the target system.



### Question 1
What command will give us a listing of all files and folders in a specified path?

The answer is "tree /F".

### Question 2
What command will print my current working directory onto the console?

The answer is "cd".

## Working with Directories and Files - CMD

### Commands:
md - make new directory
mkdir - make new directory
rd - delete directory
rmdir - delete directory
rd /S - to delete directory and it's content
rmdir /S - to delete directory and it's content
move - move directory and its content from source to destination
xcopy - copies directory and content from source to destination
xcopy {PATH_TO_SOURCE_FOLDER} {PATH_TO_DESTINATION_FOLDER} /E - The /E copies any files and subdirectories to include empty directories, xcopy will reset any attribute the file had. If you want to retain the file's attributes (such as read-only or hidden), u can use /K.

#### xcopy note:
From a hacker's perspective, xcopy can be extremely helpful. If we wish to move a file, even a system file, or something locked, xcopy can do this without adding other tools to the host. As a defender, this is a great way to grab a copy of a file and retain the same state for analysis. For example, you wish to grab a read-only file that was transferred in from a CD or flash drive, and you now suspect it of performing suspicious actions.

robocopy - Robocopy can copy and move files locally, to different drives, and even across a network while retaining the file data and attributes to include timestamps, ownership, ACLs, and any flags set like hidden or read-only

#### robocopy note:
Robocopy can also work with system, read-only, and hidden files. As a user, this can be problematic if we do not have the SeBackupPrivilege and auditing privilege attributes. This could stop us from duplicating or moving files and directories. There is a bit of a workaround, however. We can utilize the /MIR switch to permit ourselves to copy the files we need temporarily.
 
more - view content of a file
more /S - blank space will be downgraded to a single line for easier readability
openfiles
type
echo
fsutil
ren
rename
replace
\> - create file if it doesnt exist or overwrite file if it does
\>> - append to a file
< - pass a for example a text file into a command (find /i "see" < test.txt)
| - pipeline
& - issue command and follow it with another command (ping 8.8.8.8 & type test.txt)
&& - AND
|| - OR
del
erase

#### del/erase note:
if you want to delete a read-only or hidden file, you can use the /A: switch.
To delete read-only file /A:R

u can use the dir /A:R to show all files with Read-only attribute.

removing file: del /A:H * - * is any file
del /F - to force deletion of a directory

copy - copying files from source to destination
copy /V - valdiation that it worked


### Question 1
What command can display the contents of a file and redirect the contents of the file into another file or to the console?

The answer is "type".

### Question 2
What command can be used to make the 'apples' directory? (full command as answer, not the alias)

The answer is "mkdir apples".

## Gathering System Information

Gathering system information aka host enumeration

The goal of host enumeration is to provide a overall picture of the target host, its environment, and how it interacts with other systems across the network.

The first question to ask ourselves is: "How do we know what to look for?"

To answer this question, we need to have a basic understanding of all the different types of information available to us on a system.

![Types of information](info.png)

![Description of types of information](info_descri.png)

During enumeration, ask yourselves these questions:
- What system information can we pull from our target host?
- What other system(s) is our target host interacting with over the network?
- What user account(s) do we have access to, and what information is accessible from the account(s)?

Gathering all the information we can on a system or environment should be prioritized over exploiting the system, to avoid writing the system off as not vulnerable or completetly patched. Take your time gathering all the info needed.

### How to get this information?

#### Casting a Wide Net
Use the command **systeminfo** to find information about the host, such as hostname, IP address(es), domain, hotfixes that have been installed and much more. This is valuable information for a sysadmin when trying to diagnose issues.

For a hacker, this a good way to get a lay of the land while leaving a minimal footprint. Running one command is always better than running multiple commands to get the same information. We are less likely to be detected this way. Gathering information about OS version, hotfixes installed and OS build version can quickly help us determine if the host is vulnerable to an exploit through a Google or ExploitDB search.

#### Systeminfo Output
It's not a good idea to only know one way to gather information, escpially if they are monitored or tracked more closely. That is why we need multiple ways to gather the required information while staying under the radar.

![systeminfo command and output](image.png)

#### Examining the System
If you need to retrieve some basic system information such as hostname or OS version, you can use the commands **hostname** and **ver**.

![hostname](image-3.png)
![ver](image-4.png)

#### Scoping the Network
You can use the command **ipconfig** to gather information about some basic networking information of our target. This will help us understand how our target is connected and what devices it can access across the network - this is a invaluable tool in our arsenal as an attacker. The ipconfig command displays all current TCP/IP network configurations for the machine.

![ipconfig](image-2.png)

If you use Ipconfig without parameters, we get network information such as Domain Name, IPv4 Address, Subnet Mask and Default Gateway.
By using **ipconfig /all** it will provide us with a fully comprehensive listing of every network adapter attached to the system and additional information, including the physical address of each adapter (MAC Address), DHCP settings and DNS servers.

If you need information about what hosts our target has come into contact with, use the command **arp**.
Arp displays the contents and entries contained within the Address Resolution Protocol (ARP) cache. You can also use this command to modifiy the table entries. 

![arp /a](image-1.png)

#### Understanding Our Current User
To figure out your current user, command **whoami**.

Whoami displays user, group and privilege information for the current logged in user.

The output of this command is the current domain and user named of the logged in account. Note: If the current user is not a domain-joined account, the NetBIOS name will be provided instead.
![whoami](image-5.png)

To check for the user's security privileges on the system, the command **whoami /priv** can be used. This is a set of basic permissions, but if there is any misconfigurations here, that could be used to escalate priviledges.

![whoami /priv](image-6.png)

You can also check what groups the account is member of by using the command **whoami /groups**. This can provide information about what groups the account is part of, default groups and more importantly custom groups which the user have access to.

![whoami /groups](image-7.png)

Command **whoami /all** can also be used to provide alot more information, like user, groups and priviledges.

#### Investigating Other Users/Groups
Most environments have machines that are on domain-joined networks, which means that anyone can log into any physical host on the network without requiring a local account on the machine. We can use this to our advantage to scope out what users have accessed our current host to see if we could access other accounts. We can use the command **net** to do this.

Net user allows us to display a list of all users on a host, information on a specific user and to create or delete users.

![net user](image-8.png)

We can also look at what groups exist across the network by using commands **net group** or **net localgroup**.
Net group will display any groups that exist on the host from which we issued the command, create and delete groups and add or remove users from groups. It will also display domain group information if the host is joined to the domain. Net group must be run against a domain server such as the DC, while net localgroup can be run against any host to show us the groups it contains.

![net group vs net localgroup](image-9.png)

#### Exploring Resources on the Network
You can also gather information about the shares on a server that the user has access to and keep yourself able to log in again if you lose an established connection.

The command **net share** allows us to display info about the shared resources on the host and to create new shared resources.

![net share](image-10.png)

In the picture above you can see a share named Records, this can be potentially intersting informatioon for us to enumerate. If you do find a share like this we need to keep track of the following:
- Do we have the proper permissions to access this share?
- Can we read, write, and execute files on the share?
- Is there any valuable data on the share?

Shares are also good for hosting anything and lateral movement across hosts, if you need to be sneaky, you can drop a payload onto the share to enable movement around other hosts on the network.

If you don't need to look at shares but wish to search the environment broadly, use command **net view**.
Net view will display any shared resources the host you are issuing the command against knows of. This includes domain resources, shares, printers and more.

#### Piecing Things Together
Now you know  how to extracts tons of information, but keep in mind that this is quite noisy, and will most likely be noticed by anyone semi-competent. As it stands, we are writing tons of logs, leaving traces across multiple hosts and have little to no insight into what their Endpoint Dectection and Response (EDR) and Network Intrustion Detection System (NIDS) are able to see.

Note: cmd-prompt in a standard environment is not a common thing for a regular user. Administrators somtimes have reasons to use it, but it will be very suspicious if a average user is executing cmd.exe. With that in mind, using *net \** commands within an environment is not a normal thing either, and can be one way to alert on potential infiltration of a networked host easily. With proper monitoring and logging enabled, we should spot these actions quickly and use them to triage an incident before it gets too far out of hand.

### Question 1
What command will output verbose system information such as OS configuration, security info, hardware info, and more?

The answer is "systeminfo".

### Question 2
Access the target host and run the 'hostname' command. What is the hostname?

The answer is "ICL-WIN11".

## Finding Files and Directories

### Where Command
Command **where** can search for files in our environment variable path. If you use *where calc.exe* it will show us the path to where the file is, however it only works because calc.exe is in our environment path. If you are looking for a file that is not in the environment path, you can use the prefix */R*, this prefix will specify which directory to search for and will dig through all directories within that path.

![where command](image-11.png)

![recursive where](image-12.png)

Can also use wildcard *\** when searching.

![wildcard where](image-13.png)

### Find Command
The command **find** is used to search for text strings within a file or files. You can also pipeline the output in terminal to use find, but the command is limited to when it comes to using wildcard patterns in its matching. 

![find command](image-14.png)

Prefix */V* - a NOT clause
Prefix */N* - display line numbers
Prefix */I* - ignore case sensitivity

![using find prefixes](image-15.png)

### Findstr Command
Is similiar to find command but it searches through files but for patterns instead. It will look for anything matching a pattern, regex value, wildcards and more. *Findstr == grep* command for Linux, kinda.

