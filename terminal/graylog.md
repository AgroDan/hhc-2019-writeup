# Graylog

## Question 1:

**C:\Users\minty\Downloads\cookie_recipe.exe**

*From: EventID:2 AND minty AND firefox.exe -- found cookie_recipe.exe*

We can find this searching for sysmon file creation event id 2 with a process named firefox.exe
and not junk .temp files. We can use regular expressions to include or exclude patterns:

`TargetFilename:/.+\.pdf/`

## Question 2:

**192.168.247.175:4444**

*From: EventID:3 AND cookie_recipe.exe*

We can pivot off the answer to our first question using the binary path as our ProcessImage.


## Question 3:

**whoami**

*From: EventID:1 AND cookie_recipe.exe*

Since all commands (sysmon event id 1) by the attacker are initially running through the
cookie_recipe.exe binary, we can set its full-path as our ParentProcessImage to find child
processes it creates sorting on timestamp.

## Question 4:

**webexservice**

*From the same, follow the trail*

Continuing on using the cookie_recipe.exe binary as our ParentProcessImage, we should see
some more commands later on related to a service.

## Question 5:

**C:\cookie.exe**

*From the same, follow the trail*

The attacker elevates privileges using the vulnerable webexservice to run a file called
cookie_recipe2.exe. Let's use this binary path in our ParentProcessImage search.

## Question 6:

**Alabaster**

*From EventID:4624 AND SourceNetworkAddress:192.168.247.175*

Windows Event Id 4624 is generated when a user network logon occurs successfully. We can
also filter on the attacker's IP using SourceNetworkAddress.

## Question 7:

**06:04:28**

*From: LogonType:10 AND EventID:4624*

LogonType 10 is used for successful network connections using the RDP client.

## Question 8:

*Answer: elfu-res-wks2,elfu-res-wks3,3*

The attacker has GUI access to workstation 2 via RDP. They likely use this GUI connection
to access the file system of of workstation 3 using explorer.exe via UNC file paths (which
is why we don't see any cmd.exe or powershell.exe process creates). However, we still see
the successful network authentication for this with event id 4624 and logon type 3.

**So: EventID:4624 AND source:elfu-res-wks3**

## Question 9:

**C:\Users\alabaster\Desktop\super_secret_elfu_research.pdf**

We can look for sysmon file creation event id of 2 with a source of workstation 2. We can
also use regex to filter out overly common file paths using something like:

`AND NOT TargetFilename:/.+AppData.+/`

*EventID:3 AND DestinationPort:3389*

## Question 10:

**104.22.3.84**

*From: alabaster AND EventID:3*

Connecting from DEFANELF (192.168.247.175) => elfu-res-wks2 (192.168.247.176)



Attacker's machine:

http://192.168.247.175
