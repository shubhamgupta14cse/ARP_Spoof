import scapy.all as scapy


def sniff(interface):
    scapy.sniff(iface=interface, store=False,prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)

sniff(enter the interface to sniff upon)
