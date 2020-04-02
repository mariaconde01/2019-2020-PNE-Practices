from Client0 import Client
from Seq1 import*

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.149"
PORT1 = 8080
PORT2 = 8081

# -- Create a client object
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
print(c1)
print(c2)

folder= "../session-04/"
filename = folder+ "FRAT1.txt"
s = Seq()
sequence=s.read_fasta(filename)
sequence = str(sequence)
print(f"Gene FRAT1: {str(sequence)}")

Fragment1 = sequence[0:10]
Fragment2 = sequence[10:20]
Fragment3 = sequence[20:30]
Fragment4 = sequence[30:40]
Fragment5 = sequence[40:50]
Fragment6 = sequence[50:60]
Fragment7 = sequence[60:70]
Fragment8 = sequence[70:80]
Fragment9 = sequence[80:90]
Fragment10 = sequence[90:100]

Fragment_list = [Fragment1, Fragment2, Fragment3, Fragment4, Fragment5, Fragment6, Fragment7, Fragment8, Fragment9, Fragment10]
c1.talk(f"sending FRAT1 Gene to the server, in fragments of 10 bases...")
c2.talk(f"sending FRAT1 Gene to the server, in fragments of 10 bases...")

server_index= 0
for element in Fragment_list:
    if (server_index+1) % 2 ==0:
        c2.talk(f"Fragment{server_index+1}:{Fragment_list[server_index]}")
        server_index +=1
    else:
        c1.talk(f"Fragment{server_index+1}:{Fragment_list[server_index]}")
        server_index +=1

index = 0
for element in Fragment_list:
    print(f"Fragment {index+ 1}: {Fragment_list[index]}")
    index +=1

