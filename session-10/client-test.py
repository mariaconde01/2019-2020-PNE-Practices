from Client0 import Client

IP = "192.168.1.149"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

for counter in range(5):
    print("To Server: ", end="")
    termcolor.cprint(f"Message {counter}", "blue")
    print("From Server:", end="")
    termcolor.cprint(c.debug_talk(f"ECHO: Message {counter}"))

