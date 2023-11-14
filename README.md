# Migration of private repos to public - Partial list

## CheatSheet

### Windows Administration
```
sfc /scannow # check windows for errors
```
```
Powershell Start Notepad.exe -ArgumentList "C:\\Windows\\System32\\drivers\\etc\\hosts"
```
```
 New-Object System.Net.Sockets.TcpClient("192.168.0.6", 3389)
```
```
Cipher /w:<PATH> # wipe free space
```
```
Certutil -encode <filepath> <outputfile> # encode/decode in base64
```
```
taskkill /f /t /im "<MSASCuiL.exe/MSASCui.exe>" # stops ms defender
```

### Encoding & Cryptography

```
[System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("H"))  # base64 
```
```
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String(SA==')) # base64
```
```
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(SA==')) # base64
```

## Architecture & Design
- https://www.inkandswitch.com/local-first/

# Tools
## Penetration Testing

## Defence & Threat Hunting

- IPS & IDS
	- Zeek
	- Snort
	- Suricata

- Threat hunting
 	- Sigma
  	- Yara
	- ssdeep
	- APTSimulator

- EDRs - MDFI, Crowdstrike

- Forensics
	- Sleuth kit 
	- Volatility


## Computer Networks
- **Common Protocols Implementations**
	- NAT & DHCP
		- ICS,
  		- dhcpcd(ISC DHCP)
    		- dnsmas
 	- DNS
  		- BIND(most common, de facto standard), Unbound, Dnsmasq, MS DNS

- **Remote Access** - SSH/mosh , RDP, VNC (usually use passwords/private key for authentication) 

- **VPN Protocols**
	- Wireguard
	- sshuttle/openssh TUN(P2P)
	- OpenVPN(P2S)
	- IPSec(S2S)
	- SDN Protocols
	- IP Tunneling/SIT 

- Proxies
	 - Reverse(web) proxies 
		 - nginx  
		 - apache
		 - haproxy
		 - caddy
## General
- **Applications**
	- **CLI & TUI** - Cmus, Aria2, nnn, ranger
	- **Collaboration & Session sharing** - Atom share, ttyd
- **Programming**
	- Code Editors - Vim, VSCodium, Notepad++, Limetext  
	- IDEs -
