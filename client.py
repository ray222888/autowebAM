import socket
import time
import os
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)
server.bind(("", 44444))
casesport = sys.argv[1]


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", int(casesport)))
while True:
 data, addr = client.recvfrom(1024)
 print("received message: %s"%data)
 #do something
 os.system("./test.sh")
 print("test start")
