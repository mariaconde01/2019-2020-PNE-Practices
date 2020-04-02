
from Client0 import Client
from Seq1 import*

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.149"
PORT =8081

# -- Create a client object
c = Client(IP, PORT)
print(c)

folder= "../session-04/"
filename = folder+ "FRAT1.txt"
s = Seq()
sequence=s.read_fasta(filename)
sequence = str(sequence)
print(f"Gene FRAT1: {str(sequence)}")

# -- Send a message to the server
c.talk(f" Sending FRAT1 Gene to the server, in fragments of 10 bases...")

c.talk(f"Fragment 1: {sequence[0:10]}")
print(f"Fragment 1: {sequence[0:10]}")

c.talk(f"Fragment 2: {sequence[10:20]}")
print(f"Fragment 2: {sequence[10:20]}")

c.talk(f"Fragment 3: {sequence[20:30]}")
print(f"Fragment 3: {sequence[20:30]}")

c.talk(f"Fragment 4: {sequence[30:40]}")
print(f"Fragment 4: {sequence[30:40]}")

c.talk(f"Fragment 5: {sequence[40:50]}")
print(f"Fragment 5: {sequence[40:50]}")
