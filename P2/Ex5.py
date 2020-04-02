
from Client0 import Client
from Seq1 import*

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.149"
PORT =8081

# -- Create a client object
c = Client(IP, PORT)
print(c)

folder= "../session-04/"
filename = folder+ "U5.txt"
s = Seq()
sequence=s.read_fasta(filename)


c.debug_talk("Sending the U5 Gene to the server..")
c.debug_talk(str(sequence))