from Crypto.Util.number import *
from flag import flag

flag = bytes_to_long(flag.encode('utf-8'))

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 3
c = pow(flag,e,n)

print(f"{n = }")
print(f"{e = }")
print(f"{c = }")

