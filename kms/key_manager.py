import secrets

_KEY_STORE = {}

def get_key(service_name):
    if service_name not in _KEY_STORE:
        _KEY_STORE[service_name] = secrets.token_bytes(32)
    return _KEY_STORE[service_name]
