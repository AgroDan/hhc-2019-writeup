# Analysis with JQ

This calls for using only jq to find the destination IP in Zeek
logs that has the greatest duration, pointing to a supposed C&C
server. The line to obtain this was:
	
`$ jq -s -c 'sort_by(.duration)[]' ./conn.log | tail -50`
	
The last IP there was 13.107.21.200 since it had the longest
duration.