import socket

IP = "192.168.1.149"
PORT = 8080

#WE CREATE THE SOCKET
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ESTABLISHING THE CONNECTION WITH THE SERVER
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

#receive data from the server
msg = s.recv(2000)

print("Message from the server: \n")
print(msg.decode("utf-8"))
#closing the connection
s.close()





