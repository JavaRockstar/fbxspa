# Fbxspa
Cross Site Port Attack (XSPA), which is a type of SSRF attack.
In such a scenario, the attacker can insert port specific payloads and scan a target machine using the vulnerable server. Worse, instead of scanning some other target machine the payloads can be crafted which will be directed to the same vulnerable server itself. In this case, the HTTP packets are sent from the server to itself and the application sends the response to the attacker. By analyzing the responses (response error/time delay), the port status of the vulnerable server can be determined

fbxspa is a simple tool which exploit facebook api calls to scan the ports of other domain as well as internal Ip range of facebook.
only http and https were whitelisted  else it would be possile to map file://, ftp://,ssh:// too
it could  be useful in origin spoofing attacks.
### Version
1.0

### Note :
##This tool is just built for security test  purpose don't misuse it author  will not be responsible for your actions its .

### Usage

```sh
$ python fbxspa.py
```

```sh
$ Enter the host ip 192.168.1.5
$ 1.)Default scan 
$ 2.)Specify the range
$ option>>> 2
$ start_port>>> 21
$ end_port>>> 80
$ Scanning started
[+]Port 21 open
[+]Port 21 closed
.......



```

### Imports

* sys
* requests


### Development

Want to contribute? Great!

Feel free to use or edit the code 


License
----

MIT


**Free Software, Hell Yeah!**

**Resources to read about XSPA**
[Reference links]: # (These are reference links for xspa)
  http://media.blackhat.com/bh-us-12/Briefings/Polyakov/BH_US_12_Polyakov_SSRF_Business_Slides.pdf
  http://niiconsulting.com/checkmate/2015/04/server-side-request-forgery-ssrf/
  https://ibreak.software/2012/11/07/cross-site-port-attacks-xspa-part-1/
