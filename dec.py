import hashlib
import math
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


p = int("0xde26ab651b92a129", 16)
g = int("0x2", 16)

A = int("0x1315098dadf0c284", 16)
B = int("0xaeb85a071e33ff5d", 16)



def pollard_rho(g, h, p):

    n = p - 1

    def step(x, a, b):

        r = x % 3

        if r == 0:
            return (
                (x * g) % p,
                (a + 1) % n,
                b
            )

        elif r == 1:
            return (
                (x * h) % p,
                a,
                (b + 1) % n
            )

        else:
            # x = x^2
            return (
                (x * x) % p,
                (2 * a) % n,
                (2 * b) % n
            )

    x = 1
    a = 0
    b = 0

    X, A, B = x, a, b

    while True:

        x, a, b = step(x, a, b)

        X, A, B = step(X, A, B)
        X, A, B = step(X, A, B)

        if x == X:

         

            numerator = (a - A) % n
            denominator = (B - b) % n

            try:
                inv = pow(denominator, -1, n)
            except ValueError:
                x = 1
                a = 0
                b = 0
                X, A, B = x, a, b
                continue

            secret = (numerator * inv) % n

            if pow(g, secret, p) == h:
                return secret


print("[+] Starting Pollard Rho...")

b = pollard_rho(g, B, p)

print("[+] Bob's private b =", b)



shared_secret = pow(A, b, p)

print("[+] Shared secret =", shared_secret)


# SHA1 -> AES key

key = hashlib.sha1(
    str(shared_secret).encode()
).digest()[:16]

print("[+] AES key =", key.hex())


# AES-CBC

iv = bytes.fromhex(
    "2d5b69aec2c30f248d1b2a024784b782"
)

ciphertext = bytes.fromhex(
    "337f4ffee826938c37e94a8b8b0b278bc01b1aafb745413c8bd549527780c60f"
)

cipher = AES.new(
    key,
    AES.MODE_CBC,
    iv
)

plaintext = cipher.decrypt(ciphertext)

print("[+] Plaintext:", plaintext)

try:
    flag = unpad(plaintext, AES.block_size)
    print("[+] FLAG:", flag.decode())
except ValueError:
    print("[-] Padding error")