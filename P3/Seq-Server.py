import socket
import termcolor
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8080

LIST_SEQ=["AGTACGGTAACGTAGACGTTACGATTGATGTACTTGATATGTATTT","GTGAGGTACCTGTACGTTTAACGATGTACGTAGGTGCACC","TGACACGGTCACTGAGTCATGCACGTAATGCATGGTGCACGTAAGCGGGTG","CGTACGTAACATGCCGATGCTAGTACCGTACGATGTCACGTAGTCGCTCGTCGTCGTGCA","CAGTTTTTTTTTGTACCGTAACGTACGTCGTCGCGTGTCGGTGCCGGCTGTCGGCGCTGGTCGCG"]
FOLDER= r"C:\\Users\maria\PycharmProjects\2019-2020-PNE-Practices\session-04\\"
TXT = ".txt"
LIST_GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

def GET(index):
   return LIST_SEQ[index]

def INFO(seq):

   seq = Seq(seq)
   lenS = seq.len()
   A_COUNTER = seq.count_base('A')
   G_COUNTER = seq.count_base('G')
   C_COUNTER = seq.count_base('C')
   T_COUNTER = seq.count_base('T')
   A_PER = 100 * A_COUNTER / lenS
   G_PER = 100 * G_COUNTER / lenS
   C_PER = 100 * C_COUNTER / lenS
   T_PER = 100 * T_COUNTER / lenS

   RES = f"Sequence: {seq}\nTotal length: {lenS}\nA: {A_COUNTER} ({A_PER}%)\nC: {C_COUNTER} ({C_PER}%)\nG: {G_COUNTER} ({G_PER}%)\nT: {T_COUNTER} ({T_PER}%)\n"
   return RES

def COMP(seq):
   seq = Seq(seq)
   return seq.complement()


def REV(seq):
   seq = Seq(seq)
   return seq.reverse()


def GENE(GENE):
   seq = Seq(GENE)
   seq = Seq(seq.read_fasta(FOLDER + GENE + TXT))
   return str(seq)


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
    # -- Waits for a client to connect
   print("Waiting for clients....")
   try:
       (cs, client_ip_port) = ls.accept()
   # -- Server stopped manually
   except KeyboardInterrupt:
       print("Server Stopped!")
       # -- Close the listening socket
       ls.close()
       exit()
   else:

       # -- Read the message from the client
       # -- The received message is in raw bytes
       req_raw = cs.recv(2000)
       req = req_raw.decode()

       # ------ Process the command
       # -- Remove the \n
       lines = req.split("\n")
       line0 = lines[0].strip()
       # -- Separate the line into command an argument
       # -- Eliminate the blank spaces
       lcmds = line0.split(' ')

       # -- The first element is the command
       com = lcmds[0]

       # -- Get the first argument
       try:
           argument = lcmds[1]
       except IndexError:
           argument = ""

       res = ""

       if com == "PING":
           print("PING command!")
           res = "OK!"
       elif com == "GET":
           print("GET")
           res = GET(int(argument))
       elif com == "INFO":
           print("INFO")
           res = INFO(argument)
       elif com == "COMP":
           print("COMP")
           res = COMP(argument)
       elif com == "REV":
           print("REV")
           res = REV(argument)
       elif com == "GENE":
           print("GENE")
           res = GENE(argument)
       else:
           termcolor.cprint("Unknown command!!", "red")
           res = "Unknown command"

       # -- Send the response message
       res += "\n"
       print(res)
       # Client console
       cs.send(res.encode())
       # -- Close the data socket
       cs.close()


