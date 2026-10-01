from Crypto.Cipher import AES
from hashlib import sha1
from Crypto.Util.number import long_to_bytes

shared = 2204323822403222804

iv = bytes.fromhex("01124713e828f9027e6ea27a4ed05ee5")
ct = bytes.fromhex(
    "9bb4ba0fd43ebd9a5b1a09e37b0b081bee93a85b8f8a1e6c8ab1636d4951449c"
)

secret = long_to_bytes(shared)

key = sha1(secret).digest()[:16]

print("shared:", shared)
print("secret:", secret.hex())
print("key:", key.hex())

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ct)

print("raw:", pt)
print("hex:", pt.hex())