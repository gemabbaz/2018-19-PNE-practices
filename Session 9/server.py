import socket
import termcolor
import sys
# Configure the Server's IP and PORT
PORT = 8089
IP = "212.128.253.101"
MAX_OPEN_REQUESTS = 5

def process_client(cs): #The parameter will be the socket for communicating with the client
    # Read client message.
    msg = cs.recv(2048).decode("utf-8")

    termcolor.cprint(msg, 'blue')
    if msg == 'EXIT':
        sys.exit(0)

    cs.send(str.encode(msg)) #We have to decode and then code again
    #Sending message to the client
    # Close the socket
    cs.close()

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

