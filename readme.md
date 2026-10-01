Received: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
DH1536=>p=>1536bit 
2^1536 ≤ p < 2^1536
HOW TO MITM 
Alice:
DH1536, DH1024, DH512, DH256, DH128, DH64
             ↓
          Attacker
             ↓
         DH64 selected
             ↓
          cracker 
p = 0xde26ab651b92a129
g = 0x2
A = 0x1315098dadf0c284
B = 0xaeb85a071e33ff5d

ALICE=g^a mod p
BOB =g^b mod p