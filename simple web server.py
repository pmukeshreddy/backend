import socket

my_scoket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #--->make phone call
my_scoket.connect(("data.pr4e.org",80))
cmd = "GET http://data.pr4e.org/page1.htm HTPP/1.0\r\n\r\n".encode() # since data is sent in utf-8
my_scoket.send(cmd)

while True:
    data = my_scoket.recv(512)
    if len(data)<1:
        break
    print(data.decode(),end="")
my_scoket.close()
