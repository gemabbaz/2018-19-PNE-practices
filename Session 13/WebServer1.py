import http.server
import socketserver

# Define the Server's port
PORT = 8001

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")
        return


Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    httpd.serve_forever()