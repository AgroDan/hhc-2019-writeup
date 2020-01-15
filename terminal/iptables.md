# Configuring IPTables for Kent Tinseltooth

The rules to change IPTables are as follows:

1. Set the default policies to DROP for the INPUT, FORWARD, and OUTPUT chains.
2. Create a rule to ACCEPT all connections that are ESTABLISHED,RELATED on the INPUT and the OUTPUT chains.
3. Create a rule to ACCEPT only remote source IP address 172.19.0.225 to access the local SSH server (on port 22).
4. Create a rule to ACCEPT any source IP to the local TCP services on ports 21 and 80.
5. Create a rule to ACCEPT all OUTPUT traffic with a destination TCP port of 80.
6. Create a rule applied to the INPUT chain to ACCEPT all traffic from the lo interface.

With sudo, I can change IPTables. So let's start on the basics first

- Set the default policies to drop for INPUT/OUTPUT/FORWARD chains:

```
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP
sudo iptables -P FORWARD DROP
```

- Create a rule to ACCEPT all connections that are ESTABLISHED,RELATED on the INPUT and OUTPUT chains

```
sudo iptables -A INPUT -p tcp -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m state --state ESTABLISHED,RELATED -j ACCEPT
```

- Create a rule to ACCEPT only remote source IP address 172.19.0.225 to access the local SSH server (on port 22).

```
sudo iptables -A INPUT -p tcp -s 172.19.0.225/32 -m state --state NEW --dport 22 -j ACCEPT
```

- Create a rule to ACCEPT any source IP to the local TCP services on ports 21 and 80

```
sudo iptables -A INPUT -p tcp -m multiport --dports 21,80 -j ACCEPT
```

- Create a rule to ACCEPT all OUTPUT traffic with a destination TCP port of 80

```
sudo iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
```

- Create a rule applied to the INPUT chain to ACCEPT all traffic from the lo interface

```
sudo iptables -A INPUT -i lo -j ACCEPT
```

Doing this officially hardened the IOT Smart Braces Firewall.
