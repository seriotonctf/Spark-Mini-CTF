from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from binascii import hexlify,unhexlify
import base64

# put the values from the description here. Make sure they are inside b""
encrypted_flag = b"pdl3hAmvBFVFcdeFQmwB4CttDlH1tqECmML1BLV9kuc="
key = b"R34LLYSTR0NGK3Y!" 
iv = b"randomiv12345678"

base64_decoded_flag = base64.b64decode(encrypted_flag)

cipher = AES.new(key,AES.MODE_CBC,iv)
padded_flag = cipher.decrypt(base64_decoded_flag)

flag = unpad(padded_flag,AES.block_size)

print(flag)
