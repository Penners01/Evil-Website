import http.server
import socketserver

PORT = 9090


class theHttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '../www/index.html'
        return super().do_GET()

handler = theHttpHandler

my_server = socketserver.TCPServer(("", PORT), handler)

my_server.serve_forever()








with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()