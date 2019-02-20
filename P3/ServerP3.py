import socket
import termcolor
from SeqP3 import Seq
# Configure the Server's IP and PORT
PORT = 8082
IP = "212.128.253.107"
MAX_OPEN_REQUESTS = 5

def process_client(cs): #The parameter will be the socket for communicating with the client
    # Read client message.
    msg = cs.recv(2048).decode("utf-8")

    termcolor.cprint("Message from the client: {}".format(msg), 'blue')
    if msg == ' ':
        hola = "I'M ALIVE"
        cs.send(str.encode(hola))
    else:
        list = msg.split("\n")
        seq = Seq(list[0])
        for i in range(len(list)):
            if list[i] == "len":
                length = seq.len()
                message = "The total length of the sequence is: " + str(length)
                cs.send(str.encode(message))

    s.close()



# create a socket for connecting with the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept() #Once the client is connected it will print the IP

    #. . . Process the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)