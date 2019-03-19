import http.server
import socketserver
import termcolor
from SeqP6 import Seq


#Server's port
PORT = 8006


def ok_bases(seq):  # Checking that the sequence is correct (taken from practice 3)
    bases = 'ACTG'
    for i in seq: #If the input does not contain A,C,G or T, return false.
        if i not in bases:
            return False
    return True

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self): #IMPORTANT: We have to use this name

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        if self.path == "/":
            file = open("form1.html")
            contents = file.read()
            file.close()
        elif "msg" in self.path:
            echo = self.path.split("&")
            seq1 = echo[0][echo[0].find("=")+1:] #Selecting the sequence we'll work with
            if ok_bases(seq1):
                contents = <"""!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>Linked Servers</title>
                            </head>
                            <body style="background-color: tomato">
                              <h1>ECHO SERVER MESSAGE RECEIVED</h1>
                              <h2>{}</h2>
                              <h2>{}</h2>
                              <h2>{}</h2>
                              <a href="/">[Main page]</a>
                            </body>
                            </html.>""")
                lengthmsg = ""
                task1 = "" #Creating empty variables to fill them up with the correct messages
                task2 = ""
                task1 += "The sequence introduced is: " + str(seq1)#Printing in the page where info is displayed the sequence introduced

                for i in range(len(echo)):
                    if "chk=on" in echo[i]: #If the user uses the task length
                        length = seq.len() #Using the length function imported from the Practice 3
                        lengthmsg += "The length of your sequence is: " + str(length) #Printing the information
                    elif "base" in echo[i]:
                        b1 = echo[i].split("=")
                        base1 = b1[1]
                    elif "operation" in echo[i]:
                        operation1 = echo[i].split("=")
                        if operation1[1] == "perc":
                            perc = seq.perc(base1)
                            task2 += "The percentage of base" + base1 + "is" + str(perc)
                        elif operation1[1] == "count":
                            counter = seq.strbases.count(base1)
                            task2 += "Your base shows up" + str(counter) + "times in the sequence"




            contents = contents.format(lengthmsg, task1, task2)


            else:
                file = open("error.html")
                contents = file.read()
                file.close()
        else:
            file = open("error.html")
            contents = file.read
            file.close()


        self.send_response(200)  # -- Status line: OK!
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT: {}".format(PORT))

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")