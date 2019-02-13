#We are gonna create the client program using the Seq class created in the previous practice

import socket
from Seq import Seq
IP = "212.128.253.64"
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

while True:
    chat = input("Introduce your message: ")
    if chat == "Bye":
        break
    s1 = Seq(chat)
    s2 = s1.complement()
    s3 = s1.reverse()
    s.send(str.encode(s2))
    s.send(str.encode(s3))

    msg = s.recv(2048).decode("utf-8")
    msg1 = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER: \n")
    print(msg)
    s.close()
