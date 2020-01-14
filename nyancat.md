# Challenge with nyancat and Chattr

As the elf user, I noticed alabaster_snowball's shell was pointing to /bin/nsh,
which was a compiled program that displayed nyancat. I also had sudo NOPASSWD
rights to /usr/bin/chattr. /bin/nsh was immutable (as discovered by lsattr), so
I ran:

`sudo /usr/bin/chattr -i /bin/nsh`

then

`cp /bin/bash /bin/nsh`
