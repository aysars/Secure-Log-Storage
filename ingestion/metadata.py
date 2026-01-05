import time
import socket

def add_metadata(log, source):
    return {
        "timestamp": time.time(),
        "host": socket.gethostname(),
        "source": source,
        "message": log
    }
