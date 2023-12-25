# Migration of private repos to public - Partial list

**Hi! Happy learning ^_^**


# Resources

<details>
	<summary><h2>Learning</h2></summary>
	
- https://www.hacksplaining.com/owasp
	</details>

<details>
	<summary><h2>RSS</h2></summary>
	
- https://cyber.bgu.ac.il/advanced-cyber/
- https://news.ycombinator.com/
- https://www.darkreading.com/
- https://thehackernews.com/
- https://www.digitalwhisper.co.il/
- https://www.csoonline.com/
- https://leanpub.com/
	</details>

# CheatSheet

<details>
	<summary><h3>Python</h3></summary>

<details>
	<summary><h4>General</h4></summary>

  <details open>
    <summary><h5>Features</h5></summary>
 
- **`python.exe`** - console(terminal) app for **CLI** Scripts
- **`pythonw.exe`** - GUI app for **GUI/No UI** scripts
	</details>
  
  <details open>
	<summary><h5>Language Behaviour</h5></summary>

- General
 	- Every statement Ends with a NEWLINE. **Everything is a statement.**  
	- Default  Python Character Encoding - **UTF-8** 
 	- Python ignores empty lines, it uses tabs or 4 spaces for indention.
- Variable handling
	- **assignment** - assigns value to a variable using a **new pointer**. for **mutable** and **immutables**.
	- **value change** - changes the value **inside** a **memory address**, only for **mutables.**
- Security Risks
	- Difference between modules:	
		- **os.system** --> injects a shell and runs the command in it, security risk for **shell injections**.
		- **Subprocess.call** --> spawns a process and runs the command.
	- String Formatting might introduce security vulnerabilities, template strings are safer and are best for user-supplied strings.
 	- exec() - vulnerable when the code running inside it is external or untrusted/changeable by the user.
  </details>
</details>

  <details>
	<summary><h4>alternative way to search module name</h4></summary>

```python
import sys;[m for m in sys.stdlib_module_names if "<name>" in m]  # search module name
```
  </details>

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
	<summary><h3>Linux</h3></summary>
	
<details>
	<summary><h4>Administration</h4></summary>

```zsh
dhclient -r eth renew # or release
dhcpcd # dhcp
```

</details>
</details>

<details>
	<summary><h3>Windows</h3></summary>
<details>
	<summary><h4>Shell Enumeration</h4></summary>
	
```cmd
(dir 2>&1 *`\|echo CMD);&<# rem #>echo ($PSVersionTable).PSEdition # check if shell is CMD or PS
```

</details>
<details>
	<summary><h4>Windows Administration</h4></summary>

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
</details>
<details>
	<summary><h4>Encoding & Cryptography</h4></summary>

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
</details>

## Architecture & Design
- https://www.inkandswitch.com/local-first/

# Tools
## Penetration Testing

## Defence & Threat Hunting
<details>
	<summary>IPS & IDS</summary>
	
	- Zeek
	- Snort
	- Suricata
</details>

<details>
	<summary>Threat hunting</summary>
	
	- Sigma
	- Yara
	- ssdeep
	- APTSimulator
 
</details>

- EDRs - MDFI, Crowdstrike

- Forensics
	- Sleuth kit 
	- Volatility


## Computer Networks
- <details>
	<summary><b>Common Protocols Implementations</b></summary>
	
	- NAT & DHCP
		- ICS,
  		- dhcpcd(ISC DHCP)
    		- dnsmas
 	- DNS
  		- BIND(most common, de facto standard), Unbound, Dnsmasq, MS DNS
</details>
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
