import hashlib

def generate_wpa_key(passphrase, ssid):
    """Generates a WPA key using PBKDF2."""
    return hashlib.pbkdf2_hmac('sha1', passphrase.encode(), ssid.encode(), 4096, 32)

def crack_wpa(handshake_hash, ssid, wordlist):
    """Attempts to crack a WPA password using a wordlist."""
    with open(wordlist, "r") as file:
        for word in file.readlines():
            word = word.strip()
            wpa_key = generate_wpa_key(word, ssid)
            if wpa_key.hex() == handshake_hash:
                print(f"Password found: {word}")
                return word
    print("No match found.")
    return None

# Example usage:
# crack_wpa("your_handshake_hash", "WiFi-SSID", "wordlist.txt")
