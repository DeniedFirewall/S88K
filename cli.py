import argparse
from S88K import sniffer, deauth, handshake, WPAD

def main():
    parser = argparse.ArgumentParser(description="S88K - Wi-Fi Pentesting Library")
    parser.add_argument("--scan", help="Scan for Wi-Fi networks", action="store_true")
    parser.add_argument("--deauth", nargs=2, metavar=("TARGET_MAC", "ROUTER_MAC"), help="Perform a deauth attack")
    parser.add_argument("--handshake", help="Capture WPA handshake", action="store_true")
    parser.add_argument("--crack", nargs=3, metavar=("HASH", "SSID", "WORDLIST"), help="Crack WPA password using WPAD")

    args = parser.parse_args()

    if args.scan:
        print("[*] Starting Wi-Fi scan...")
        sniffer.sniff_wifi()

    elif args.deauth:
        target_mac, router_mac = args.deauth
        print(f"[*] Sending deauth packets to {target_mac} via {router_mac}...")
        deauth.send_deauth(target_mac, router_mac)

    elif args.handshake:
        print("[*] Listening for WPA handshakes...")
        handshake.capture_handshake()

    elif args.crack:
        hash_file, ssid, wordlist = args.crack
        print(f"[*] Cracking WPA password for SSID {ssid} using wordlist {wordlist}...")
        WPAD.crack_wpa(hash_file, ssid, wordlist)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
