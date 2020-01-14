# Web Apps: A TrailHead -- Holiday Hack Trail

After inspecting the talk about webapps, a very brief glimpse of the backend
code of the "Oregon Trail" game was visible, and based on that I was able to
determine how to generate a hash that the game relied on to determine if the
form parameters have been tampered with. It turns out that the hash was MD5,
and the only form vars that were hashed was the sum of the following
parameters: 

- Money 
- Distance 
- Current Day 
- Current Month 
- Current Amount of Reindeer 
- Runners 
- Ammo 
- Meds 
- Food 

Based on this, I was able to create a python script that generated a valid hash,
so you could freely tamper with any of these variables as long as you validate
properly. I was able to generate a hash using this script I created:

[hasher.py](hasher.py)

Based on the above, I opened the Developer Console in Firefox and manipulated the
hidden form variables to change my distance to 7999, keep all the other values
the same, and update the resulting hash from the above script. Once I changed that
and hit "Go," I immediately made it to the North Pole and won the game on hard
difficulty! 
