import socket
import termcolor


IP = "192.168.1.149"
PORT =8080

#step 1: creating the socket
ls=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#step 2: bind the socket to the servers ip adress and port
ls.bind((IP, PORT))


#step 3: convert into a listening socket
ls.listen()

print("Server is configured")
number_con = 0

while True:
    print("Waiting for Clients to connect")

    try:
        # step 4: wait for client to connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server is done")
        ls.close()
        exit()
    else:
        number_con += 1
        print("CONNECTION: {}. From the IP: {}".format(number_con, client_ip_port))
        # step 5: receiving info from the clinet
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f" Message received: ", end="")
        termcolor.cprint(msg, "green")

        # step 6: send a response message to the client
        response = "ECHO:" + msg
        cs.send(response.encode())

        cs.close()
