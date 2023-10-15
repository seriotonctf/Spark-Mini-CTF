enc = bytes.fromhex('11322330293911732c252e711d003b36711d1a72103f')


for i in range(256):
	flag = bytes(c ^ i for c in enc)
	if b'Spark{' in flag:
		print(f'[+] Flag: {flag}')
		print(f'[+] Key: {i}')
		break

'''
[+] Flag: b'Spark{S1ngl3_Byt3_X0R}'
[+] Key: 66
'''