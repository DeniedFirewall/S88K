import socket
import struct

def create_raw_socket(interface="wlan0mon"):
    """Creates a raw socket for capturing Wi-Fi packets."""
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    sock.bind((interface, 0))
    return sock

def parse_80211_frame(frame):
    """Extracts MAC addresses from an 802.11 frame."""
    if len(frame) < 24:
        return None, None, None
    _, _, addr1, addr2, addr3, _ = struct.unpack("!HH6s6s6sH", frame[:24])
    return addr1, addr2, addr3

def extract_ssid(frame):
    """Extracts SSID from a beacon frame."""
    if frame[0] != 0x80:  # Check if it's a beacon frame
        return None
    ssid_length = frame[37]
    return frame[38:38+ssid_length].decode(errors="ignore")

def sniff_wifi(interface="wlan0mon"):
    """Captures Wi-Fi packets and extracts SSID info."""
    sock = create_raw_socket(interface)
    print("Sniffing Wi-Fi packets...")

    while True:
        packet, _ = sock.recvfrom(4096)
        ssid = extract_ssid(packet)
        if ssid:
            addr1, addr2, addr3 = parse_80211_frame(packet)
            print(f"SSID: {ssid}, BSSID: {addr2.hex(':')}")
