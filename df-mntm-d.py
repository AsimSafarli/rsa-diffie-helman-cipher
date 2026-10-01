from sage.all import *

p = 0xde26ab651b92a129
g = 0x2

A = 0x1e94d157829a1619
B = 0x9676640a777fc711

a = discrete_log(Mod(A, p), Mod(g, p))

shared = power_mod(B, a, p)

print("a =", a)
print("shared =", shared)