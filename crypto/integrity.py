import hmac
import hashlib

def generate_hmac(data, key):
    return hmac.new(key, data, hashlib.sha256).digest()

def verify_hmac(data, mac, key):
    return hmac.compare_digest(
        generate_hmac(data, key),
        mac
    )
