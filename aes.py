# !pip install pycryptodome
from Crypto.Cipher import AES
import base64

def encrypt_AES(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext)
    ciphertext = cipher.encrypt(padded_plaintext.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_AES(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded_ciphertext = base64.b64decode(ciphertext)
    decrypted_text = unpad(cipher.decrypt(decoded_ciphertext))
    return decrypted_text.decode('utf-8')

def pad(s):
    block_size = AES.block_size
    padding_size = block_size - len(s) % block_size
    padding = chr(padding_size) * padding_size
    return s + padding

def unpad(s):
    if isinstance(s, bytes):
        padding_size = s[-1]
    else:
        padding_size = ord(s[-1])
    return s[:-padding_size]

encryption_key = b'ThisIsA16ByteKey'  # Update the key with the appropriate length
# plaintext = "Hello, AES!"
# encrypted = encrypt_AES(encryption_key, plaintext)
# decrypted = decrypt_AES(encryption_key, encrypted)

# print("Plaintext:", plaintext)
# print("Encrypted:", encrypted)
# print("Decrypted:", decrypted)
