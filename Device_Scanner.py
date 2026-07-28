# ======================
# === Device Scanner ===
# ======================

import socket
import uuid
import platform
import psutil

print("\n======================")
print("=== Device Scanner ===")
print("======================")

# _________________________________________________________________________________________________

# --- Device Name ---

device_name = socket.gethostname()

# _________________________________________________________________________________________________

# --- IP Address ---

try:
    ip_address = socket.gethostbyname(device_name)
except:
    ip_address = "Unavailable"
    
# _________________________________________________________________________________________________

# --- MAC Address ---

mac = uuid.getnode()
mac_address = ':'.join(f"{(mac >> ele) & 0xff:02X}" for ele in range(40, -1, -8))

# _________________________________________________________________________________________________

# --- Operating System ---

operating_system = f"{platform.system()} {platform.release()}"

# _________________________________________________________________________________________________

# --- CPU Information ---

processor = platform.processor()

physical_cores = psutil.cpu_count(logical=False)
logical_cores = psutil.cpu_count(logical=True)

cpu_usage = psutil.cpu_percent(interval=1)

# _________________________________________________________________________________________________

# --- RAM Information ---

memory = psutil.virtual_memory()

total_ram = memory.total / (1024 ** 3)
available_ram = memory.available / (1024 ** 3)
used_ram = memory.used / (1024 ** 3)

# _________________________________________________________________________________________________

# --- Storage Information ---

disk = psutil.disk_usage("/")

total_storage = disk.total / (1024 ** 3)
used_storage = disk.used / (1024 ** 3)
free_storage = disk.free / (1024 ** 3)

# _________________________________________________________________________________________________

# --- Display Information ---

print("\n--- Device Information ---\n")

print(f"Device Name      : {device_name}")
print(f"IP Address       : {ip_address}")
print(f"MAC Address      : {mac_address}")
print(f"Operating System : {operating_system}")

print("\n--- CPU ---\n")

print(f"Processor        : {processor}")
print(f"Physical Cores   : {physical_cores}")
print(f"Logical Cores    : {logical_cores}")
print(f"CPU Usage        : {cpu_usage}%")

print("\n--- Memory ---\n")

print(f"Installed RAM    : {total_ram:.2f} GB")
print(f"Used RAM         : {used_ram:.2f} GB")
print(f"Available RAM    : {available_ram:.2f} GB")

print("\n--- Storage ---\n")

print(f"Total Storage    : {total_storage:.2f} GB")
print(f"Used Storage     : {used_storage:.2f} GB")
print(f"Free Storage     : {free_storage:.2f} GB")

print("\nAnalysis Complete")

# _________________________________________________________________________________________________