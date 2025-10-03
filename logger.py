def log_message(message):
    print(fLOG: {message})
import datetime

def log_message(message):
    timestamp = datetime.datetime.now().isoformat()
    print(f[{timestamp}] LOG: {message})

