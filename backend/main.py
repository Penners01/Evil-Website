import http.server
import socketserver

PORT = 9090


class theHttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '../www/evil.html'
        return super().do_GET()

handler = theHttpHandler

my_server = socketserver.TCPServer(("", PORT), handler) 


def main():
    my_server.serve_forever()

if __name__ == "__main__":
    main()

    

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()