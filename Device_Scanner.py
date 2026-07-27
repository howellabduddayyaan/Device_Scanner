# ======================
# === Device Scanner ===
# ======================

import socket
import uuid

print("\n======================")
print("=== Device Scanner ===")
print("======================")


device_name = socket.gethostname()

# _________________________________________________________________________________________________

try:
    ip_address = socket.gethostbyname(device_name)
except:
    ip_address = "Unavailable"
    
# _________________________________________________________________________________________________

mac = uuid.getnode()
mac_address = ':'.join(f"{(mac >> ele) & 0xff:02X}" for ele in range(40, -1, -8))

# _________________________________________________________________________________________________



