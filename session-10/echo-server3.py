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
c_counter=0
ip_client_list=[]

while True:
        # -- Wait for a client to connect
        print("Waiting for Clients to connect")
        try:
            (cs, client_ip_port) = ls.accept()

        except KeyboardInterrupt:
            print("Server is done")
            ls.close()
            exit()

        else:
            c_counter +=1
            print(f"CONNECTION {c_counter}. Client IP, PORT: {client_ip_port}")
            ip_client_list.append(client_ip_port)

            msg_raw = cs.recv(2000)
            msg = msg_raw.decode()

            print(f" Message received: ", end="")
            termcolor.cprint(msg, "green")

            response = "ECHO: " + msg
            cs.send(response.encode())

            if c_counter == 5:
                print("The following clients has connected to the server: ")
                clients = 0
                for i in ip_client_list:
                    print(f"Client {clients}: {ip_client_list[c_counter - 1]}")
                    clients += 1

            cs.close()
