import scapy.all as scp

def getmac(ip):
    req=scp.ARP(pdst=ip)
    brod=scp.Ether(dst='ff:ff:ff:ff:ff:ff')
    request=brod/req
    a=scp.srp(request,timeout=1,verbose=False)[0]
    return a

def scan():
    a=getmac('10.0.2.1/24')
    print('IP\t\t\tMAC ADDRESS\n------------------------------------------------------------------------------')
    for e in a:
        print(e[1].psrc+'\t\t'+e[1].hwsrc)
        print('------------------------------------------------------------------------------')

scan()
