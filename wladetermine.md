# Windows Log Analysis: Determine Attacker Technique

Downloading the log file and reviewing it with eql (Event Query Language)
showed that the attacker ran a password spray against 127.0.0.1/IPC$ to
determine a valid account, then uploaded a powershell one liner (which
looked suspiciously like the output of a unicorn payload). Upon obtaining
NT AUTHORITY\SYSTEM the attacker ran 
`ntdsutil.exe \"ac I ntds\" ifm \"create full c:\\hive\" q q` to interrogate
lsass.exe and obtain password hashes.
