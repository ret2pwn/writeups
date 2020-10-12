from pwn import *
import random

#switch the comment from the remote line to the process line to run this against a server instead of the file on your host
#p = remote('chals.damctf.xyz', 31932)
p = process('./schlage')


#all of the for loops were used to print the lock
for i in range(0, 19):
    print(p.recvline())


#passes pin3
p.sendline('3')
print(p.recvline())
p.sendline('3449466328')

for i in range(0, 18):
    print(p.recvline())

#passes pin 1
p.sendline('1')
p.sendline('99')

for i in range(0, 19):
    print(p.recvline())

#passes pin5
p.sendline('5')
p.sendline('1413036362')

for i in range(0, 19):
    print(p.recvline())

p.sendline('2')
for i in range(0, 2):
    print(p.recvline())

#gets seed value and passes in to our own c program running rand() with this seed
seed_value = p.recvline().decode("utf-8")

r = process("./rand")
print(r.recvline())
print(r.recvline())
r.sendline(seed_value)
rand_result = r.recvline().decode("utf-8").strip()

#these are important for pin4
rand_number = int(r.recvline().decode("utf-8").strip())
xor_var = rand_number % 10 + 0x41

print(xor_var)
input_1 = (xor_var^ord('(')) *2

#passes pin2
p.sendline(rand_result)


for i in range(0, 19):
    print(p.recvline())

#passes pin4 if xor_var == 68
p.sendline('4')
print(p.recvline())

if(xor_var == 68):
    p.sendline('helloto')
    p.interactive()
