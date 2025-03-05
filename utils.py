import socket
import struct

def create_raw_socket(interface="wlan0mon"):
    """Creates and binds a raw socket for Wi-Fi packet capture or injection."""
    try:
        sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        sock.bind((interface, 0))
        return sock
    except PermissionError:
        print("[!] Permission denied. Run as root (sudo).")
        exit(1)

def mac_address(bytes_mac):
    """Converts a raw MAC address (bytes) into human-readable format."""
    return ':'.join(f"{b:02x}" for b in bytes_mac)

def parse_80211_frame(frame):
    """Extracts MAC addresses from an 802.11 frame."""
    if len(frame) < 24:
        return None, None, None
    _, _, addr1, addr2, addr3, _ = struct.unpack("!HH6s6s6sH", frame[:24])
    return mac_address(addr1), mac_address(addr2), mac_address(addr3)
