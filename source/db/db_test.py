# Testador do CRUD by xvierdev
import db
import hashlib

# Calcula o Hash de uma string
def hash_text(text):
    """Hashes a text using SHA-256."""
    return hashlib.sha256(text.encode()).hexdigest()

# Rotinas de teste do CRUD

db.insert_user('Wesley', hash_text('Serveless'))
print(db.read_user('Wesley', hash_text('fubaka')))
print(db.update_user('Wesley', hash_text('fubaka')))
print(db.read_user('Wesley', hash_text('fubaka')))
print(db.delete_user('Wesley'))
print(db.read_user('Wesley', hash_text('fubaka')))