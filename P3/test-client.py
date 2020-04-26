from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

LIST_GENES=["U5","ADA","FRAT1","FXN","RNU6_269P"]

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(c)

#PING
print("* Testing PING...")
print(c.talk("PING"))
#TEST GET
print("* Testing GET...")
for index in range(5):
   com = f"GET {index}"
   print(f"{com}: {c.talk(com)}")
#INFO
seq = c.talk("GET 0")
print("* Testing INFO...")
com = f"INFO {seq}"
print(c.talk(com))
#TEST COMP
print("* Testing COMP...")
com = f"COMP {seq}"
print(com)
print(c.talk(com))
#TEST REV
print("* Testing REV...")
cmd = f"REV {seq}"
print(com)
print(c.talk(com))
#TEST GENE
print("* Testing GENE...")
for GEN in LIST_GENES:
   com= f"GENE {GEN}"
   print(com)
   print(c.talk(com))

