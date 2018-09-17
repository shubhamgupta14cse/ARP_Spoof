# ARP_Spoof
A powerful python script that lets you spoof the ARP table , sniff packets and discover devices MAC and ip on your local network.


## Library used 

* SCAPY
* time




## Getting Started

To set up the project in your local enivironment ,first clone the repository and save it on your local environment/machine.
To run the program edit the t,v and interface variable in the code.
go to the below mentioned code and enter the ip of the target machine , victim machine and the interface your connected to e.g wlan0,eth0
you can do ifconfig in linux or mac and ipconfig/all on window to discover your interface.
To get the target and victim url just go to the network_scan.py program run it and it would tell you all the devices connected on your network.
Always enter the target url to be the url of your router or wi-fi and victim ip to be the device you want to sniff data of.

```
t=#enter the target ip you want to spoof/fool(eg router)
v=#enter the victim ip you want target to assume you for(eg any divice conecceted on your network)
interface=#enter the interface to sniff the packet upon
```

After entering target and victim ip go to the bottom of the code to find
```
#do_spoof(t,v)
#do_restore(t,v)
#sniff(interface)
```

And remove to un comment the code do spoof and sniff to spoof and then sniff data and then afterwards do_restore to restore back the ARP table of target and victim machine.
