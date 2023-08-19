import http.server
import socketserver
import random

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        start = int(post_data.split('&')[0].split('=')[1])
        end = int(post_data.split('&')[1].split('=')[1])
        result = random.randint(start, end)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(result).encode('utf-8'))

if __name__ == '__main__':
    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print(f"Server running on port {PORT}")
        httpd.serve_forever()

