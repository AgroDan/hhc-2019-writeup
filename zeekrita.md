# Network Log Analysis -- From Zeek to RITA

The next step was to search through the Bro/Zeek logs and find a beaconing
system that is almost certainly infected with the use of RITA, or Real
Intelligence Threat Analysis. RITA is a program developed by the good folks
at Black Hills Infosec, and a personal project of John Strand. This
application is free and can be used to find "weird connections" and other
oddities from Bro/Zeek logs.

Kringlecon provided a set of the Bro/Zeek logs for this exercise. I unpacked
them in a directory on my Kali VM and cloned Rita from
activecountermeasures.com's github repo. I followed the directions to install
from a docker image and ran the following commands to get it to work:

```
client:~# docker-compose run --rm rita import /logs elfu
client:~# docker-compose run rita show-databases
elfu
client:~# docker-compose run rita show-beacons elfu

<< snip lots of data >>

client:~# docker-compose run rita show-beacons elfu -H | head -100
```

It produced the following:
[Rita data](images/hhc-rita.jpeg)

This IP, according to Rita, is almost 100% certain to be a beacon based on the
amount of connections, the interval disparity, and how many connections within
this time slot. The answer to the question of "which IP address is infected
with malware" is 192.168.134.130.
