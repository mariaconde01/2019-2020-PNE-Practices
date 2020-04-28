import http.server
import socketserver
import termcolor
import pathlib

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def reading_fasta(file):
   # -- Open and read the html files
   file_contents = pathlib.Path(file).read_text().split("\n")[1:]
   body = "".join(file_contents)
   return body


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

   def do_GET(self):
       """This method is called whenever the client invokes the GET method
       in the HTTP protocol request"""

       # Print the request line
       termcolor.cprint(self.requestline,"green")

       # Message to send back to the client:
       FOLDER =r"C:\\Users\maria\PycharmProjects\2019-2020-PNE-Practices\session-14\\"
       if self.path == "/" or self.path == "/index.html":
           FILE = "Index.html"

       elif "/green" in self.path:
           FILE = "Green.html"

       elif "/pink" in self.path:
           FILE = "Pink.html"

       elif "/blue" in self.path:
           FILE = "Blue.html"

       else:
           FILE = "Error.html"

       contents = reading_fasta(FOLDER + FILE)

       # Generating the response message

       if self.path == "/" or self.path == "/index.html":
           self.send_response(200)  # -- Status line: OK!

       elif "/green" or "/blue" or "/pink" in self.path:
           self.send_response(200)  # -- Status line: OK!

       else:
           self.send_response(404)  # -- Status line: ERROR NOT FOUND

       # Define the content-type header:
       self.send_header('Content-Type', 'text/html')
       self.send_header('Content-Length', len(contents.encode()))

       # The header is finished
       self.end_headers()

       # Send the response message
       self.wfile.write(contents.encode())

       return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
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
       print("Stopped by the user")
       httpd.server_close()

