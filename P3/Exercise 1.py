import socket
from termcolor import colored
from Seq1 import Seq

#GET function
SEQ_list=["ACGCCTAGTCA","ACTGAATGGACTCAG","TTGCATGGCAAGCT","CGGTAAGCTACG","GTCCGAATGCAT"]
def GET(seq_n):
    for i in list_seq:
        if seq_n ==list_seq.index(i):
            return i
#INFO function
BASE_list=["A","C","G","T"]
def INFO(seq):
    seq= Seq(seq)
    return seq.count(BASE_list)



# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"
list_seq=["ATCGAATGAC","CTGGATACG","TAGTCAAGCT","AATGTAGCA","GTGACCTACG"]
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()
        if msg == "PING":
            print(colored("PING COMMAND","green"))
            response = "OK!\n"
            cs.send(response.encode())
            cs.close()
        elif msg.split(" ")[0]=="GET":
            print(colored("GET COMMAND", "green"))
            seq= int(msg.split(" ")[1])
            res= GET(seq)
            cs.send(res.encode())
            cs.close()
        elif msg.split(" ")[0]=="INFO":
            print(colored("INFO COMMAND", "green"))
            seq = msg.split(" ")[1]
            res = INFO(seq)
            [[key, value]] = ((str(key), str(value)) for key, value in response.items())
            final_res= key + ":" + value
            cs.send(final_res.encode())
            cs.close()






