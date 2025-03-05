import socket

def create_raw_socket(interface="wlan0mon"):
    """Creates a raw socket for listening to Wi-Fi packets."""
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    sock.bind((interface, 0))
    return sock

def detect_handshake(packet):
    """Detects WPA handshakes by looking for EAPOL packets."""
    if b"\x88\x8e" in packet:  # Check for EAPOL
        print("Captured WPA handshake!")
        with open("handshake.pcap", "ab") as f:
            f.write(packet)

def capture_handshake(interface="wlan0mon"):
    """Listens for WPA handshakes."""
    sock = create_raw_socket(interface)
    print("Listening for WPA handshakes...")

    while True:
        pkt, _ = sock.recvfrom(4096)
        detect_handshake(pkt)
