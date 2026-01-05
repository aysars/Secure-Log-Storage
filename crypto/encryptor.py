import json
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_log(data, key):
    aes = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aes.encrypt(
        nonce,
        json.dumps(data).encode(),
        None
    )
    return nonce + ciphertext
