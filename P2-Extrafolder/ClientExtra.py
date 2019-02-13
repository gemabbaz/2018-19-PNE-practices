#We are gonna create the client program using the Seq class created in the previous practice
import socket
from Seq import Seq
#Here is the IP address of my computer
IP = "212.128.253.106"
PORT = 8081 #Chose the port 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

while True:
    chat = input("Introduce your message: ")
    if chat == "Bye": #To close the program
        break
    s.send(str.encode(chat)) #Sending the output to the server
    msg = s.recv(2048).decode("utf-8")

    print("MESSAGE FROM THE SERVER: \n")
    print(msg)
    s.close()