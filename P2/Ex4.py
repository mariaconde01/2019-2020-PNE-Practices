from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.149"
PORT ="8080"

# -- Create a client object
c = Client(IP, PORT)
print(c)
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
c.debug_talk ( " Mensaje 1 --- ", "green")
c.debug_talk ( " Mensaje 2: Testing !!! " , "green")
print(f"Response: {response}")
