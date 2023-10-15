p1 = 'Srdt3__u0tsyhc'
p2 = 'pk0_lmy_th__43a{ntl30g_1bcn}'

flag = ''

for c in range(42):
    if c%3 == 0:
        flag += p1[c//3]
    elif c%3 == 1:
        flag += p2[c//3]
    else:
        flag += p2[c//3 + 14]

print(flag)

# Spark{d0nt_t3ll_m3_y0u_g0t_th1s_by_ch4nc3}