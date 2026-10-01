from hashlib import sha1
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

shared = 2204323822403222804

iv = bytes.fromhex(
    "01124713e828f9027e6ea27a4ed05ee5"
)

ciphertext = bytes.fromhex(
    "9bb4ba0fd43ebd9a5b1a09e37b0b081bee93a85b8f8a1e6c8ab1636d4951449c"
)

key = sha1(str(shared).encode("ascii")).digest()[:16]

print("AES key:", key.hex())

cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = cipher.decrypt(ciphertext)

print("raw:", plaintext)

plaintext = unpad(plaintext, 16)

print("FLAG:", plaintext.decode())