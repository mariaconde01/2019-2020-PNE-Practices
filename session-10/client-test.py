from Client0 import Client

IP ="192.168.1.149"
PORT = 8080

c = Client(IP, PORT)

for a in range(5):
    c.debug_talk(f"Message {a}")

