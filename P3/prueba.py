import socket

#--- testing.....

# SERVER IP, PORT
IP = "212.128.253.107"
PORT = 8083

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))    # Before connecting to the server, ask the user for the string
    lines = []
    msg = input()
    while True:
        msg = input()
        if msg and msg.strip():
            lines.append(msg)
        else:
            break

    if len(lines) == 0:
        lines = " "
    for i in range(len(lines)):
        s.send(str.encode(lines[i]))


    # Receive the servers respoinse
    response = s.recv(2048).decode("utf-8")


    print(response)


    s.close()