from socket import *

def createserver():
    serverscoket = socket(AF_INET,SOCK_STREAM)
    try:
        serverscoket.bind(("localhost",9000)) #-----> bind socket with particluar address and port number
        serverscoket.listen(5)
        while (1):
            (client_socket,client_address) = serverscoket.accept()
            rd = client_socket.recv(5000).decode()
            pices = rd.split("\n")
            if (len(pices)>0): print(pices[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type:text/html;charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>hello world</body></head>\r\n\r\n"
            client_socket.sendall(data.encode())
            client_address.shutdown(SHUT_WR) #--> TELLS THAT THE SENDING PORTION IS SHUT DOWN

    except KeyboardInterrupt:
        print("shutdowning")

    except Exception as ex:
        print(ex)
    serverscoket.close()


createserver()