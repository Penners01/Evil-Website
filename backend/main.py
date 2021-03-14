import http.server
import socketserver

PORT = 9090
handler = http.server.SimpleHTTPRequestHandler(directory="../www")

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()