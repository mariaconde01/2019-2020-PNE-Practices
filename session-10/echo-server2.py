import socket

IP= "212.128.253.175"
PORT= 8082
count=0

#step 1: creating the socket
ls=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#step 2: bind the socket to the servers ip adress and port
ls.bind((IP, PORT))


#step 3: convert into a listening socket
ls.listen()

print("Server is configured")

while True:
    try:
        # step 4: wait for client to connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server is done")
        ls.close()
        exit()
    else:
        # step 5: receiving info from the clinet
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        count +=1

        print("connection", count)
        print("received message: {msg}")
        print("client_IP_PORT:", client_ip_port)

        # step 6: send a response message to the client
        response = f"ECHO: {msg} \n"
        cs.send(response.encode())

        cs.close()
