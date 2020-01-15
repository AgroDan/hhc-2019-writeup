# Linux Path Challenge

Figuring out the Linux Path Challenge was really simple.
All that you had to do was list the contents of the
current directory. Unfortunately running the ls command
returned the statement "This isn't the ls you're looking
for." This signified that the version of ls that was in
your path wasn't the standard `ls` command. All you had
to do was find the real ls command. Running `which ls`
would print that you were running `/usr/local/bin/ls`,
which is nonstandard.

Running `find / -name ls 2>/dev/null` returned an ls
command in `/bin/ls`, so running that by calling it
directly would solve the challenge.

[ls challenge](../images/hhc-linuxpath.png)
