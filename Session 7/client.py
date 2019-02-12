#We are programming our fiest client
import socket

IP= "212.128.253.64"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # WE WANT TO CREATE a socket
                                                   #for communicating thru iternet
                                             #and is caled AF_INET

s.connect((IP, PORT))

s.send(str.encode("HEY"))

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER: \n")
print(msg)
s.close()
