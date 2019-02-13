import socket

while True:
    chat = input("Say something: ")
    if chat == 'End':
        break
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = "212.128.253.107"
    PORT = 8080

    s.connect((IP, PORT))
    s.send(str.encode(chat))

    msg = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER: \n")
    print(msg)
    s.close()