from scapy.all import ICMP,IP,sr

if __name__=="__main__":
    src_ip="192.168.44.132"
    dest_ip="1.1.1.1"
    ip_layer=IP(src=src_ip, dst=dest_ip)
    print(ip_layer.show())
    icmp_req=ICMP(id=100)
    packet=ip_layer/icmp_req
    response,_=sr(packet,iface="eth0")
    if response:
        response.show()
