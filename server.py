import socket
import time
import ReadExcel
from time import sleep
import serverSend

serverSend.serverSend(44411,37021)
serverSend.serverSend(44412,37022)
serverSend.serverSend(44413,37023)
serverSend.serverSend(44414,37024)
serverSend.serverSend(44415,37025)
serverSend.serverSend(44416,37026)

#receive test result
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
while True:
    data, addr = client.recvfrom(1024)
    print("received message: %s"%data)
    try:
     ReadExcel.excelUpdate(data)
    except Exception as ex: print (ex)
    sleep(2)