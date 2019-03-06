import http.server
import socketserver

# Define the Server's port
PORT = 8002

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")
        print("Request line" + self.requestline)
        print("       Cmd:  " + self.command)
        print("Path:  " + self.path)
        if self.path == "/":
            file = open("index.html")
            content = file.read()
            file.close()
        elif self.path == "/pink.html":
            file = open("pink.html")
            content = file.read()
            file.close()
        elif self.path == "/blue.html":
            file = open("blue.html")
            content = file.read()
            file.close()
        elif self.path == "/green.html":
            file = open("green.html")
            content = file.read()
            file.close()
        else:
            file = open("error.html")
            content = file.read()
            file.close()

        self.send_response(200);
        self.send_header('Content-Type','text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))
        return


Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:

        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
