# SRF Admin Portal

Obtained credentials by downloading https://srf.elfu.org/README.md
	
```
username: admin
password: 924158F9522B3744F5FCD4D10FAC4356
```
	
To query properly, I used this:
	
`# jq '.[] | select(.method == "GET")' ./http.log`
		
and
		
`# jq '.[] | select(.method == "GET") | select(.status_code == 200)' ./http.log`
	
You can obtain the API to manipulate the data some more from here: http://srf.elfu.org/apidocs.pdf
	
`curl -s -b "srfsession=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm91dGUiOmZhbHNlLCJydWxlcyI6IkE6MC4wLjAuMC8wIn0.5IR6qZ1NZG_EMKUQi0HjOGacc3ePVFlHCYECEKf7GMI" 'https://srf.elfu.org/api/weather?station_id=*'`