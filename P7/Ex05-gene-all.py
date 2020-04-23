import http.client
import json
import termcolor
from Seq1 import Seq

DICT_GENES = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060','RNU6_269P': 'ENSG00000212379','MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633','FGFR3': 'ENSG00000068078','KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000145362'}

LIST_BASES = ['A', 'T', 'C', 'G']

SERVER = 'rest.ensembl.org'
ENDP = '/sequence/id/'
PRMS = '?content-type=application/json'

for g in DICT_GENES:
    REQ = ENDP + DICT_GENES[g] + PRMS
    URL = SERVER + REQ

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", REQ)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    # -- Read the response message from the server
    answer = conn.getresponse()

    # -- Print the status line
    print("Response received!:", answer.status, answer.reason, "\n")

    # -- Read the response's body
    content = answer.read().decode()

    # -- Create a variable with the data,
    # -- form the JSON received
    gene = json.loads(content)

    termcolor.cprint("Gene:", "green", end="")
    print(g)
    termcolor.cprint("Description:", "green", end="")
    print(gene["desc"])

    GENE_SEQ = gene["seq"]

    seq = Seq(GENE_SEQ)
    l = seq.len()
    A_COUNTER = seq.count_base('A')
    C_COUNTER = seq.count_base('C')
    G_COUNTER = seq.count_base('G')
    T_COUNTER = seq.count_base('T')
    A_PER = 100 * A_COUNTER / l
    C_PER = 100 * C_COUNTER / l
    G_PER = 100 * G_COUNTER / l
    T_PER = 100 * T_COUNTER / l

print(f"""Total length: {l}
A: {A_COUNTER} ({A_PER}%)
G: {G_COUNTER} ({G_PER}%)
C: {C_COUNTER} ({C_PER}%)
T: {T_COUNTER} ({T_PER}%)""")

DICT_VALUES = seq.count()
LIST_VALUES = list(DICT_VALUES.values())
MAX_VAL = max(LIST_VALUES)

termcolor.cprint("Most frequent Base:","blue", end="")
print(f" {[LIST_VALUES.index(MAX_VAL)]}")
