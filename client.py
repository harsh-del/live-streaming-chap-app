import socket
import threading
import cv2
import base64

def client():
    
    s=socket.socket()

    s.connect(("192.168.29.6",8290))
    response=s.recv(100000000)
    print(response.decode())
    cap = cv2.VideoCapture(0)
    while True:
        ret , photo = cap.read()
        #cap.release()
        cv2.imwrite("client_streaming.jpg",photo)
        cv2.imshow('client',photo)
        if cv2.waitKey(100)==13:
            break
        with open("client_streaming.jpg", 'rb') as f:
            byte_image=base64.b64encode(f.read())
        s.send(byte_image)
    cv2.destroyAllWindows()
t_client=threading.Thread(target=client)
t_client.start()
