import hashlib
import datetime
import os

def now():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def clear_console():
    """Limpa o console."""
    os.system('cls' if os.name == 'nt' else 'clear')