import http.server
import socketserver
import termcolor

#Server's port
PORT = 8009


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self): #IMPORTANT: We have to use this name

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        if self.path == "/":
            file = open("form12.html")
            contents = file.read()
            file.close()
        elif '/echo' in self.path:
            if "chk=on" in self.path:
                message = self.path.split('&')[0]
                message = message.split('=')[1].upper()
            else:
                message = self.path.split('&')[0]
                message = message.split('=')[1]

            file = open("form2.html")
            echo =  message
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