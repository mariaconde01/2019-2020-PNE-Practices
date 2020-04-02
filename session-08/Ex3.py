import socket

# SERVER IP, PORT

IP = "192.168.1.149"
PORT =8080

while True:
    # -- Ask the user for a message
    m = input("Enter a message: ")

    # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send data
    s.send(str.encode(m))

    # Closing the socket
    s.close()