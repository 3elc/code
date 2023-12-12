# Migration of private repos to public - Partial list

# Resources
- https://www.hacksplaining.com/owasp

# RSS
- https://cyber.bgu.ac.il/advanced-cyber/
- https://news.ycombinator.com/
- https://www.darkreading.com/
- https://thehackernews.com/
- https://www.digitalwhisper.co.il/
- https://www.csoonline.com/
- https://leanpub.com/

## CheatSheet
<details>
	<summary><h3>Python</h3></summary>

<details>
	<summary><h4>alternative way to output stdout to var with sys module.</h4></summary>

```python
import io,sys; b=io.StringIO(); sys.stdout=b;<Command>;out = b.getvalue().splitlines(); sys.stdout=sys.__stdout__
```
</details>
<details>
	<summary><h4>get stdout from command. exec using stdout</h4></summary>

```python
exec("import io,contextlib as cl;o=io.StringIO();\nwith cl.redirect_stdout(o):\thelp(\"topics\")")`
# might be unsafe especially in production.
```
</details>
</details>
<details>
	<summary><h3>Windows</h3></summary>

#### Shell Enumeration
```
(dir 2>&1 *`\|echo CMD);&<# rem #>echo ($PSVersionTable).PSEdition # check if shell is CMD or PS
```


#### Windows Administration
```cmd
netsh int ip reset  # Reset TCP/IP
netsh int winsock reset # recover from socket errors, may remove settings
```
```cmd
netsh advf set currentprofile state off  # turn firewall off
```
```cmd
route
netstat -r # alternative
```
```cmd
getmac
```
```cmd
netstat -s -p <PROTOCOL> # statistics
```
```cmd
netstat -aonb # socket finding windows
```
```powershell
Powershell Start Notepad.exe -Verb RunAs -ArgumentList "C:\\Windows\\System32\\drivers\\etc\\hosts" &@rem edits hosts, be careful.
```
```cmd
sfc /scannow &@rem check windows for errors, be careful with this tool.
```
```powershell
 New-Object System.Net.Sockets.TcpClient("192.168.0.6", 3389)
```
```cmd
Cipher /w:<PATH> # wipes free space
```
```cmd
Certutil -encode <filepath> <outputfile> # encode/decode in base64
```
```cmd
taskkill /f /t /im "<MSASCuiL.exe/MSASCui.exe>" # stops ms defender
```

#### Encoding & Cryptography

```powershell
[System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("H")) 
```
```powershell
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String('SA=='))
```
```powershell
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('SA=='))
```
</details>

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

- **Remote Access** - SSH , RDP, VNC (usually use passwords/private key for authentication) 

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
	- IDEs 
