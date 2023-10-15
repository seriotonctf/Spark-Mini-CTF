from Crypto.Util.number import *
from flag import flag

flag = bytes_to_long(flag.encode('utf-8'))

p = getRandomNBitInteger(64)
while not isPrime(p):
    p = getRandomNBitInteger(64)

q = getRandomNBitInteger(512)
while not isPrime(q):
    q = getRandomNBitInteger(512)

n = p * q
e = 65537
c = pow(flag,e,n)

print(f"{n = }")
print(f"{c = }")
print(f"{e = }")
