from scapy.all import sniff, IP, TCP, UDP, Raw

def process_packet(packet):
    print("\n==============================")
    print(" Packet Captured")

    # IP Layer
    if packet.haslayer(IP):
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")
        print(f"TTL            : {packet[IP].ttl}")

    # TCP Layer
    if packet.haslayer(TCP):
        print("Protocol       : TCP")
        print(f"Source Port    : {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")
        print(f"Flags          : {packet[TCP].flags}")

    # UDP Layer
    elif packet.haslayer(UDP):
        print("Protocol       : UDP")
        print(f"Source Port    : {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")

    # Payload
    if packet.haslayer(Raw):
        payload = packet[Raw].load
        print(f"Payload Length : {len(payload)} bytes")
        print("Payload Preview:")
        print(payload[:80])  # show first 80 bytes only

    print("Packet Summary :", packet.summary())

print(" Starting Network Sniffer... Press Ctrl+C to stop")
sniff(prn=process_packet, store=False)