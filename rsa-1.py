from Crypto.Util.number import long_to_bytes

e = 1
ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485

pt = ct

flag = long_to_bytes(pt)

print(flag)