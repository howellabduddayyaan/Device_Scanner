# ======================
# === Device Scanner ===
# ======================

import socket

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

