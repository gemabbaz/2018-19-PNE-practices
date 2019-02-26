import socket
import termcolor

# Change this IP to yours!!!!!
IP = "212.128.253.96"
PORT = 8089
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    empty = msg.splitlines()
    empty1 = empty[0].lstrip("GET ").rstrip(" HTTP/1.1") #Here we want to delete part of the request message
    if empty1 == "":
        file = open("Index.html")
        contents = file.read()
        file.close()
    elif empty1 == "/pink":
        file = open("Pink.html")
        contents = file.read()
        file.close()
    elif empty1 == "/blue":
        file = open("Blue.html")
        contents = file.read()
        file.close()
    else:
        file = open("Error.html")
        contents = file.read()
        file.close()




    status_line = "HTTP/1.1 200 ok\r\n" #We always have to finish this line with the \r\n
    heather = "Content-Type: text/html\r\n" #Plain text when you are just sending a simple message, not an image, video etc.
    heather += "Content-Lenth {}\r\n".format(len(str.encode(contents)))

    response_msg = status_line + heather + "\n" + contents

    cs.send(str.encode(response_msg))


    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)