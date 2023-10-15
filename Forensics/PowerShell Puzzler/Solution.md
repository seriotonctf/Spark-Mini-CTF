One liner 
```bash
cat shell.ps1| base64 -d | awk -F'+' '{print $2 $4}' | cut -d ';' -f1 | sed 's/ //g' | sed "s/'//g" | base64 -d | tr -d '\n'
Spark{0n3_l1n3r_r3v3rs3_sh3ll_ftw}
```

You can also use CyberChef :)
