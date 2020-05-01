import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

   def do_GET(self):
       """This method is called whenever the client invokes the GET method
       in the HTTP protocol request"""

       # Print and analize the request line
       termcolor.cprint(self.requestline,"green")
       request = self.requestline.split(' ')

       # Get the path that always starts with "/"
       path = request[1]

       # Read the arguments
       arguments = path.split('?')

       # Get the verb
       action = arguments[0]

       # -- Content type header
       # -- Error and main page are in HTML

       if action == "/":
           contents = Path('form-EX01.html').read_text()
       elif action == "/echo":
           argument_message = arguments[1].split("=")
           message = argument_message[1]
           contents = f"""
                                           <!DOCTYPE html>
                                           <html lang = "en">
                                           <head>
                                           <meta charset = "utf-8" >
                                             <title> RESULT </title >
                                           </head >
                                           <body>
                                           <h1> Received message: </h1>
                                           <p>{message}</p>
                                           <a href="/">Main page</a>
                                           </body>
                                           </html>
                                           """
       else:
           contents = Path('Error.html').read_text()

       # Generating the response message
       self.send_response(200)  # -- Status line: OK!

       # Define the content-type header:
       self.send_header('Content-Type', 'text/html')
       self.send_header('Content-Length', len(str.encode(contents)))

       # The header is finished
       self.end_headers()

       # Send the response message
       self.wfile.write(str.encode(contents))

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
       print("Stoped by the user")
       httpd.server_close()

