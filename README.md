# Migration of private repos to public - Partial list

# Resources
- https://www.hacksplaining.com/owasp

# RSS

- https://news.ycombinator.com/
- https://www.darkreading.com/
- https://thehackernews.com/
- https://www.digitalwhisper.co.il/
- https://www.csoonline.com/
- https://leanpub.com/

## CheatSheet
### Shell Enumeration
```
(dir 2>&1 *`\|echo CMD);&<# rem #>echo ($PSVersionTable).PSEdition # check if shell is CMD or PS
```


### Windows Administration
```
sfc /scannow &@rem check windows for errors, be careful with this tool.
```
```
Powershell Start Notepad.exe -Verb RunAs -ArgumentList "C:\\Windows\\System32\\drivers\\etc\\hosts" &@rem edits hosts, be careful.
```
```
 New-Object System.Net.Sockets.TcpClient("192.168.0.6", 3389)
```
```
Cipher /w:<PATH> # wipes free space
```
```
Certutil -encode <filepath> <outputfile> # encode/decode in base64
```
```
taskkill /f /t /im "<MSASCuiL.exe/MSASCui.exe>" # stops ms defender
```

### Encoding & Cryptography

```
[System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("H")) 
```
```
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String('SA=='))
```
```
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('SA=='))
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
 	- **Linux Shells** - sh, xonsh, zsh 
- **Programming**
	- Code Editors - Vim, VSCodium, Notepad++, Limetext  
	- IDEs -


# General
- **Applications**
	- **Collaboration & Session sharing** - Atom share, ttyd

# Penetration Testing

## Network PT
- Tunnelling #tools/net/remote_access #tools/pt/net/tunnelling 
	-  Iodine,Dnscat2 
	- Stunnel(adds TLS) #tools/net/proxies 
- Proxies  
	 - Reverse(web) proxies #tools/web/implementations #tools/net/proxies
		 - nginx  
		 - apache
		 - haproxy
		 - caddy
- Vulnerability Scanners
		- Nessus
		- OpenVAS
- Port Scanners
- Packet analyzers(sniffers) #tools/net/packet_analyzers
	- [Bruteshark](https://github.com/odedshimon/BruteShark), #tools/net/forensics #tools/net/visualization  
	- [[Kismet]]  
	- [[Scapy]]  #tools/net/packet_generators #tools/net/packet_manipulation
## Web PT
- HTTP Tools & Debuggers #tools/net/HTTP  #tools/pt/web
		- [Web Devtools](Web%20Devtools.md) 
		- HTTP ToolKit 
		- HTTPie 
- Web App scanners & proxies #tools/pt/web
	- mitmproxy 
	- Burp Suite  
	- OWASP Zap(DAST) 
	-  [burp to owasp keys](Burp%20to%20OWASP%2020230517152856.png)
	- Gobuster
## Reversing & Assembly 

- Frameworks #tools/pt/re/Frameworks 
	- R2fride
	- Radare #tools/programming/disassemblers 
	- IDA  #tools/programming/disassemblers #tools/pt/re/debuggers
- R2fride #tools/pt/re/Frameworks 
- Hex Editors #tools/pt/re/hex
	- HxD
- [binary analysis](binary%20analysis.md)  #tools/pt/re/bin_analysis
	- unix - `nm`,`objdump`,`readelf`,`strings`
- [[Assemblers]] #tools/pt/re/assemblers #tools/programming/assemblers
	- x86 - nasm, GNU gas, masm(windows)
- [Debuggers](Debuggers.md)  #tools/pt/re/debuggers 
	-  [[ImmDBG]]
- [[Compilers &Decompilers]] #tools/pt/re/compilers #tools/pt/re/decompilers
	- [Compiler Explorer](https://godbolt.org) 
	- [Decompiler Explorer](https://dogbolt.org/)


## Computer Networks
- Wireless
	- **Wi-Fi**
		- python-wifi-survey-heatmap
- mosh
-  **Network Forensics & Traffic Generators**
	- Xplico
	- Ostinato
	- Flightsim
