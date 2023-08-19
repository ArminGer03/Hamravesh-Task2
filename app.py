from http.server import BaseHTTPRequestHandler, HTTPServer
import random

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/random.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('random.html', 'r') as file:
                html_content = file.read()

            self.wfile.write(html_content.encode())
        elif self.path == '/main.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('main.html', 'r') as file:
                html_content = file.read()

            self.wfile.write(html_content.encode())
        elif self.path == '/skills.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('skills.html', 'r') as file:
                html_content = file.read()

            self.wfile.write(html_content.encode())
        elif self.path == '/achievements.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('achievements.html', 'r') as file:
                html_content = file.read()

            self.wfile.write(html_content.encode())
        elif self.path == '/logo.png':
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()

            with open('logo.png', 'rb') as file:
                image_data = file.read()

            self.wfile.write(image_data)
        elif self.path == '/prof.jpeg':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()

            with open('prof.jpeg', 'rb') as file:
                image_data = file.read()

            self.wfile.write(image_data)
        elif self.path == '/styles.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()

            with open('styles.css', 'r') as file:
                css_content = file.read()

            self.wfile.write(css_content.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        num1 = int(post_data.split('&')[0].split('=')[1])
        num2 = int(post_data.split('&')[1].split('=')[1])
        random_number = random.randint(num1, num2)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with open('random.html', 'r') as file:
            html_content = file.read()

        html_content = html_content.replace('{random_number}', str(random_number))
        self.wfile.write(html_content.encode())


# Open the webpage in Chrome automatically
def open_webpage():
    webbrowser.open('http://localhost:8000/main.html')

# Run the server
def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server...')
    httpd.serve_forever()

# Start the server and open the webpage
if __name__ == '__main__':
    run()
    open_webpage()