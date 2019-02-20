import socket

#--- testing.....

# SERVER IP, PORT
IP = "212.128.253.107"
PORT = 8082

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))    # Before connecting to the server, ask the user for the string
    empty = ""
    while True:
        msg = input()+"\n"
        if msg and msg.strip():
            empty += msg
        else:
            break

    if len(empty) == 0:
        empty = " "

    s.send(str.encode(empty))


    # Receive the servers respoinse
    response = s.recv(2048).decode("utf-8")

    print("Response: {}".format(response))




    s.close()