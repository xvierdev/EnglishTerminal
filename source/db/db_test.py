# Testador do CRUD by xvierdev
import source.db.users as users
import hashlib

# Calcula o Hash de uma string
def hash_text(text):
    """Hashes a text using SHA-256."""
    return hashlib.sha256(text.encode()).hexdigest()

# Rotinas de teste do CRUD

users.insert_user('Wesley', hash_text('Serveless'))
print(users.read_user('Wesley', hash_text('fubaka')))
print(users.update_user('Wesley', hash_text('fubaka')))
print(users.read_user('Wesley', hash_text('fubaka')))
print(users.delete_user('Wesley'))
print(users.read_user('Wesley', hash_text('fubaka')))