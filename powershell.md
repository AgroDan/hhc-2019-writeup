# Powershell Challenge

This was a series of powershell challenges to align a laser.


First step was to get the recent history:

`PS > Get-History`

shows "I have many name=value variables that I share to applications system wide. At a command…"

To expand on that, use:

`PS > get-history | select-string name=value`

and it returns:

> I have many name=value variables that I share to applications system wide. At a command I will
> reveal my secrets once you Get my Child Items.

So I printed all environment variables:

`PS > Get-ChildItem env:`

And it printed a bunch, but showed one environment variable called "riddle" that was also squeezed
out of the terminal. To print it, I ran:

`PS > Write-Output $env:riddle`

Which returned:

> Squeezed and compressed I am hidden away. Expand me from my prison and I will show you the way.
> Recurse through all /etc and Sort on my LastWriteTime to reveal I'm the newest of all.

So I did just that:

`PS > Get-ChildItem -Recurse -Path /etc | sort-object LastWriteTime`

And it showed the file: /etc/apt/archive. I assumed this is a compressed file from the above hint,
so I expanded the archive by first trying to find the command:

`PS > Get-Command | select-string archive`

And I decompressed it:

`PS > Expand-Archive /etc/apt/archive`

Inside /home/elf/archive/refraction/ was a file "runme.elf". First, I had to chmod it to execute:

`PS > chmod +x ./runme.elf`

Then start it

`PS > Start-Process ./runme.elf`

It returned:

> refraction?val=1.867

Inside /home/elf/archive/refraction/riddle there was the text:

> Very shallow am I in the depths of your elf home. You can find my entity by using my md5 identity:
>
> 25520151A320B5B0D21561F92C8F6224

So to find the file in question, I created the following:

`PS > Get-ChildItem -Recurse -Path /home/elf -include *.txt | ForEach-Object { $x = Get-FileHash -Algorithm MD5 $_.fullname ; if ($x.Hash -eq "25520151A320B5B0D21561F92C8F6224") { Write-Output "We got one! := $($x.Path)" } }`

> temperature?val=-33.5

>I am one of many thousand similar txt's contained within the deepest of /home/elf/depths. Finding me
> will give you the most strength but doing so will require Piping all the FullName's to Sort Length.

I ran:

`PS > Get-ChildItem . -Recurse | Select-Object fullname | Sort-Object {$_.Fullname.Length } | ForEach-Object { $x = $_.fullname }`

And $x contained the value:

> /home/elf/depths/larger/cloud/behavior/beauty/enemy/produce/age/chair/unknown/escape/vote/long/writer/behind/ahead/thin/occasionally/explore/tape/wherever/practical/therefore/cool/plate/ice/play/truth/potatoes/beauty/fourth/careful/dawn/adult/either/burn/end/accurate/rubbed/cake/main/she/threw/eager/trip/to/soon/think/fall/is/greatest/become/accident/labor/sail/dropped/fox/0jhj5xz6.txt

It contained the contents:

> Get process information to include Username identification. Stop Process to show me you're skilled
> and in this order they must be killed:
>
> bushy
> alabaster
> minty
> holly
> 
> Do this for me and then you /shall/see .

So. I ran the following to get the associated users:

`PS > Get-Process -IncludeUserName`

Then killed them in this sequence:

`PS > Stop-Process -Id 39
PS > Stop-Process -Id 10
PS > Stop-Process -Id 64
PS > Stop-Process -Id 72`

And it printed:

> Get-Content /shall/see
> 
> Get the .xml children of /etc - an event log to be found. Group all .Id's and the last thing will be
> in the Properties of the lonely unique event Id.

Alright! So:

`PS > Get-ChildItem -Path /etc -Include *.xml -Recurse`

And it returns:

> /etc/systemd/system/timers.target.wants/EventLog.xml
>  Get-Content /etc/systemd/system/timers.target.wants/EventLog.xml


I created an xml var:

`PS > [xml]$xml = Get-Content /etc/systemd/system/timers.target.wants/EventLog.xml`

Then I grouped it based on ID's:

`PS > $grouped = $xml.Objs.Obj.Props | Group I32`

...

After a lot of research, I discovered a much better way!

`PS > $myEvents = Import-CliXml -Path /etc/systemd/system/timers.target.wants/EventLog.xml`

And then grouped it by Id to determine one single standout

`PS > $myEvents | Group Id`

It returned:

```powershell
Count Name Group

----- ---- -----

1   1 {System.Diagnostics.Eventing.Reader.EventLogRecord}

39  2 {System.Diagnostics.Eventing.Reader.EventLogRecord, System.D…

179 3 {System.Diagnostics.Eventing.Reader.EventLogRecord, System.D…

2   4 {System.Diagnostics.Eventing.Reader.EventLogRecord, System.D…

905 5 {System.Diagnostics.Eventing.Reader.EventLogRecord, System.D…

98  6 {System.Diagnostics.Eventing.Reader.EventLogRecord, System.D…
```

There's one entry with the ID of 1! So….

`PS > $myEvents | where-object {if ($_.Id -eq 1) { Write-Output $_ }}`

And it returned:

> C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -c "`$correct_gases_postbody = @{`n O=6`n H=7`n He=3`n N=4`n Ne=22`n Ar=11`n Xe=10`n F=20`n Kr=8`n Rn=9`n}`n"

So:

@{O=6;H=7;He=3;N=4;Ne=22;Ar=11;Xe=10;F=20;Kr=8;Rn=9}

Jackpot!

> Get-Content /etc/systemd/system/timers.target.wants/EventLog.xml |select-string ".Id" | Group



(iwr http://127.0.0.1:1225/api/angle?val=65.5).RawContent

(iwr http://127.0.0.1:1225/api/temperature?val=-33.5).RawContent



And don't forget to turn it on!
