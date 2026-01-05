import struct

LOG_FILE = "secure_logs.bin"

def store_log(encrypted_log, mac):
    with open(LOG_FILE, "ab") as f:
        f.write(struct.pack(">I", len(encrypted_log)))
        f.write(encrypted_log)
        f.write(mac)
