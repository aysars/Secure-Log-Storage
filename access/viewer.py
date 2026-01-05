import struct
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from crypto.integrity import verify_hmac

LOG_FILE = "secure_logs.bin"


class SecurityError(Exception):
    pass


def read_logs(key):
    logs = []

    with open(LOG_FILE, "rb") as f:
        while True:
            size_bytes = f.read(4)
            if not size_bytes:
                break

            size = struct.unpack(">I", size_bytes)[0]
            encrypted_log = f.read(size)
            mac = f.read(32)

            if not verify_hmac(encrypted_log, mac, key):
                raise SecurityError("Log integrity violation detected")

            nonce = encrypted_log[:12]
            ciphertext = encrypted_log[12:]

            aes = AESGCM(key)
            decrypted = aes.decrypt(nonce, ciphertext, None)
            logs.append(decrypted.decode())

    return logs
