#We are gonna create the client program using the Seq class created in the previous practice
import socket
from Seq import Seq
#Here is the IP address of my computer
IP = "212.128.253.106"
PORT = 8080 #Chose the port 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

while True:
    chat = input("Introduce your message: ")
    if chat == "Bye": #To close the program
        break
    s1 = Seq(chat)
    s2 = s1.complement() #Using complement function imported from Seq class
    s3 = s1.reverse() #Using complement function imported from Seq class
    text1 = "The complementary sequence is: "+s2.strbases
    text2 = "\n The reverse sequence is: "+s3.strbases
    s.send(str.encode(text1)) #Sending the output to the server
    s.send(str.encode(text2))


    msg = s.recv(2048).decode("utf-8")

    print("MESSAGE FROM THE SERVER: \n")
    print(msg)
    s.close()
