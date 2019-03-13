import http.server
import socketserver
import termcolor
from SeqP6 import Seq

#Server's port
PORT = 8006


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

            if "chk=on" in self.path:
                message = self.path.split('&')[0]
                message = message.split('=')[1]
                msg = Seq(message)
                length = msg.len()
                message = "The length of your sequence is: " + str(length)
            elif "base=A" and "operation=count" in self.path:
                message = self.path.split('&')[1][2]
                message = message.split('=')[2][3]
                msg = Seq(message)
                count_A = msg.count("A")
                message = "The number of times base A shows up in your sequence is: " + str(count_A)


            else:
                message = self.path.split('&')[0]
                message = message.split('=')[1]

            file = open("form2.html")
            echo = message
            contents = file.read().format(echo)

            file.close()

        else:
            file = open("error.html")
            contents = file.read()
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