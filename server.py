import socket
import base64
import threading
import cv2
import os

def server():
    
    s=socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    ip=""
    port=8290

    s.bind((ip,port))

    s.listen()
    c,addr=s.accept()
    c.send("connected".encode())
    k=0
    while True:
        client_data=c.recv(10000000)
        decoded_data = base64.b64decode(client_data)
        file="client_stream_{}.jpg".format(k)
        with open(file, 'wb') as f:
            f.write(decoded_data)
        image=cv2.imread(file)
        cv2.imshow('server',image)
        os.remove("client_stream_{}.jpg".format(k))
        k=k+1
        if cv2.waitKey(100)==13:
            break
    cv2.destroyAllWindows()
t_server=threading.Thread(target=server)
t_server.start()
