from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def decrypt_aes_512_cbc(key, ciphertext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key.encode()), modes.CBC(b'\x00' * 16), backend=backend)
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

# Informasi yang diberikan
key = 'MalangKotaPelajarBanyakKampus123'
ciphertext = base64.b64decode("K1T7dcLIds0QGvfj7sgjA0hXmzMTAr1I3c4g8KTXO+s52oukZFGKPl1dgxoUJyS6")

plaintext = decrypt_aes_512_cbc(key, ciphertext)
print(plaintext.decode('utf-8'))
