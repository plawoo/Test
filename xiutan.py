import socket
import threading
import time
activeDegree = dict()
flag = 1

def main():
    global activeDegree
    global flag
    HOST = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
    s.bind((HOST, 0))
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    while flag:
        data, addr = s.recvfrom(65565)
        host = addr[0]
        activeDegree[host] = activeDegree.get(host, 0) + 1
        if addr[0] != '192.168.1.102':
            print(data, addr)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    s.close()

t = threading.Thread(target=main)
t.start()
time.sleep(60)
flag = 0
t.join()
for item in activeDegree.items():
    print(item)