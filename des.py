# !pip install pycryptodome
from Crypto.Cipher import DES
import base64

def encrypt_DES(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_DES(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decoded_ciphertext = base64.b64decode(ciphertext)
    decrypted_text = unpad(cipher.decrypt(decoded_ciphertext))
    return decrypted_text.decode('utf-8')

def pad(s):
    block_size = DES.block_size
    padding_size = block_size - len(s) % block_size
    padding = chr(padding_size) * padding_size
    return s + padding

def unpad(s):
    padding_size = s[-1]
    return s[:-padding_size]

encryption_key = b'ThisIsA8'