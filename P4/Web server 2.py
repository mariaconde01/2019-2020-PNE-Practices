#All the exercises of the practice are written in a single code

import socket
import pathlib
# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080
def read_fasta(filename):
    # -- Open and read the html files
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    print(req_line)

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    FOLDER = r"C:\Users\jesus.diaz\PycharmProjects\2019-2020-PNE-Practices\P4\P4"
    file_request = req_line.split()[1]
    # file_request is like req_line (GET /info/A HTTP/1.1) only with (/info/A), (/info/C) , (/)....

    #Exercise 6
    if file_request == "/":
        filename = "\index.html"
    #Exercise 2
    elif "/info/A" in file_request:
        filename = "\A.html"
    #Exercise 3
    elif "/info/C" in file_request:
        filename = "\C.html"
    #Exercise 4
    elif "/info/G" in file_request:
        filename = "\G.html"
    elif "/info/T" in file_request:
        filename = "\T.html"
    #Exercise 5
    else:
        filename = "\error.html"

    body = read_fasta(FOLDER + filename)

    # This new contents are written in HTML language
    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()