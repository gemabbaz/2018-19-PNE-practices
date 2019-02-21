import socket
import termcolor
from SeqP3 import Seq
# Configure the Server's IP and PORT
PORT = 8097
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
        seq = (list[0]).upper()
        ok_bases(seq)
        if ok_bases(seq):
            seq = Seq(list[0])
            list.pop(0)
            for i in range(len(list)):
                if list[i] == "len":
                    length = seq.len()
                    message = "The total length of the sequence is: " + str(length) + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "complement":
                    compl = seq.complement()
                    message = "The complement sequence is: " + compl.strbases + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "reverse":
                    reverse = seq.reverse()
                    message = "The reverse sequence is: " + reverse.strbases + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "countA":
                    countA = seq.count("A")
                    message = "The number of times A shows up is: " + str(countA) + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "countC":
                    countC = seq.count("C")
                    message = "The number of times C shows up is: " + str(countC) + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "countG":
                    countG = seq.count("G")
                    message = "The number of times G shows up is: " + str(countG) + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "countT":
                    countT = seq.count("T")
                    message = "The number of times T shows up is: " + str(countT) + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "percT":
                    percT = seq.perc("T")
                    message = "The percentage of T is: " + str(percT) + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "percG":
                    percG = seq.perc("G")
                    message = "The percentage of G is: " + str(percG) + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "percC":
                    percC = seq.perc("C")
                    message = "The percentage of C is: " + str(percC) + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "percA":
                    percA = seq.perc("A")
                    message = "The percentage of A is: " + str(percA) + "\n"
                    cs.send(str.encode(message))
                elif list[i] == "":
                    pass

                else:
                    errormsg = "ERROR"
                    cs.send(str.encode(errormsg))

def ok_bases(seq):
    bases = 'ACTG'
    for i in seq:
        if i not in bases:
            message = "Not valid"
            clientsocket.send(str.encode(message))
            return False
    return True

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