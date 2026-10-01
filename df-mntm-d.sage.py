

from sage.all_cmdline import *  

_sage_const_0xde26ab651b92a129 = Integer(0xde26ab651b92a129); _sage_const_0x2 = Integer(0x2); _sage_const_0x1e94d157829a1619 = Integer(0x1e94d157829a1619); _sage_const_0x9676640a777fc711 = Integer(0x9676640a777fc711)
p = _sage_const_0xde26ab651b92a129 
g = _sage_const_0x2 
A = _sage_const_0x1e94d157829a1619 
B = _sage_const_0x9676640a777fc711 

a = discrete_log(Mod(A, p), Mod(g, p))

print("a =", a)

shared = power_mod(B, a, p)

print("shared =", shared)

