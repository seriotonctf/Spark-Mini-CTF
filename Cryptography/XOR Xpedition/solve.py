with open('output.txt','r') as f:
	enc = f.read().encode().strip()

key = 0x55

for c in enc:
	flag = c ^ 0x55
	print(chr(flag),end='')

# Spark{fun_w1th_0bfu5c4710n}