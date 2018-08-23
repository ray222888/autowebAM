import socket
import time
import ReadExcel
from time import sleep

def serverSend(ports,portd):
 server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
 server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
 server.settimeout(0.2)
 server.bind(("", ports))
 message = b"test start"
 server.sendto(message, ('<broadcast>', portd))
 print("message sent!")