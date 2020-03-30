from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.149"
PORT ="8080"

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method #probar si está conectado a Internet o no utilizando el comando ping
c.ping()

# -- Print the IP and PORTs
print(f"IP: {c.IP}, {c.PORT}")