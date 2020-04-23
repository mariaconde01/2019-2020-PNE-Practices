import http.client
import json
SERVER = 'rest.ensembl.org'
ENDP = '/info/ping'
PRMS = '?content-type=application/json'
REQ = ENDP + PRMS
URL = SERVER + REQ
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)
try:
   conn.request("GET", REQ)

except ConnectionRefusedError:
   print("ERROR! Can´t connect")
   exit()

#Read response message from the server
answer = conn.getresponse()

#Print the status line
print(f"Response received!: {answer.status} {answer.reason}\n")

#Read the response's body
content = answer.read().decode()
json_answer = json.loads(content)
ping = json_answer['ping']
if ping == 1:
   print("PING OK! The database is running!")
