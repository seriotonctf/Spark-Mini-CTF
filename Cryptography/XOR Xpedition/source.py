key = 0x55
obfuscated_flag = "[LIST OF REDACTED HEX FLAG VALUES]"

result = ''.join([chr(c ^ key) for c in obfuscated_flag])

with open('output.txt','w') as f:
    f.write(result)

