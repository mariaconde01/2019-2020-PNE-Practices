import http.client
import json
import termcolor

SERVER = 'rest.ensembl.org'
ENDP = '/sequence/id/'
PRMS = '?content-type=application/json'

DICT_GENES= {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060', 'RNU6_269P': 'ENSG00000212379','MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078','KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000145362'}

GENE_NAME = 'MIR633'
REQ = ENDP + DICT_GENES[GENE_NAME] + PRMS
URL = SERVER + REQ
print("Server:", SERVER)
print("URL:", URL)

#Connect with the server
conn = http.client.HTTPConnection(SERVER)
try:
   conn.request("GET", REQ)
except ConnectionRefusedError:
   print("ERROR! Cannot connect to the Server")
   exit()

#Read the response message from the server
answer = conn.getresponse()

#Print the status line
print("Response received!:", answer.status, answer.reason,"\n")

#Read the response's body
content = answer.read().decode()
# We create the dict with gene's info
gene = json.loads(content)
termcolor.cprint("Gene:", "green", end="")
print(GENE_NAME)
termcolor.cprint("Description:","green", end="")
print(gene["desc"])
termcolor.cprint("Bases:", "green", end="")
print(gene["seq"])
