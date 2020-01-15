# Nyanshell

As the elf user, I noticed alabaster_snowball's shell was pointing to /bin/nsh,
which was a compiled program that displayed nyancat. I also had sudo NOPASSWD
rights to /usr/bin/chattr. /bin/nsh was immutable (as discovered by lsattr), so
I ran:

`sudo /usr/bin/chattr -i /bin/nsh`

then

`cp /bin/bash /bin/nsh`

From there I logged in as alabaster_snowball and was greeted with a bash prompt
instead of the nyancat prompt.
