import socket

#clase para enviar mensajes fácilmente al servidor
#innit function

class Client:
    def __init__(self, IP, PORT):
        self.IP=IP
        self.PORT=PORT

    def ping(self):
        print("Ok!")

    def __str__(self):
        return (f"Connection to SERVER at {self.IP}, PORT: {self.PORT}")

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.IP, self.PORT))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response

    def debug_talk(self, msg):

        message = str(msg)
        response = self.talk(msg)
        print("To server:", end="")
        termcolor.cprint(msg, "blue")
        print(f"from server")
        termcolor.cprint(self.talk(msg), "green")