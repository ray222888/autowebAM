import socket
import time
import os

def resultSend(str):
 server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
 server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
 # Set a timeout so the socket does not block
 # indefinitely when trying to receive data.
 server.settimeout(0.2)
 server.bind(("", 44446))
 message = str
 server.sendto(message, ('<broadcast>', 37020))
 print("result message sent!")
