import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

PORT = 8080
# Preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

SEQ_LIST = ["AGATCGCGCCACTTCACTGCAGCCTCCGCGAAAGAGCGAAACTCCGTCTCA","TCCTTTCACTCCCAGCTCCCTGGAGTCTCTCACGTAGAATGTCCTCTCCACCCCCACCCA","CAGGAGGCTGAGGCGGGAGGATCGCTTGAGCCCAGGAGGTTGAGGCTGCAGTGAGGTGTG","CACTTGCAAATCATGCAGTTTATGTAGCATTTTCATTTAACACCTTCTCCCAACCATCTC","CTATGCTAACCCTGTGAACCGTTGCTCGCTTCTCCTTGACATCTGACGGCCTGGCCTTCT"]
FOLDER = r"C:\\Users\maria\PycharmProjects\2019-2020-PNE-Practices\session-04\\"
TXT = ".txt"
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):
   def do_GET(self):
       """This method is called whenever the client invokes the GET method
       in the HTTP protocol request"""
       termcolor.cprint(self.requestline,"green")
       req_line = self.requestline.split(' ')
       path = req_line[1]
       arguments = path.split('?')
       option = arguments[0]
       content = Path('error.html').read_text()
       cod = 404
       if option == "/":
           content = Path('form-4.html').read_text()
           cod = 200
       elif option == "/ping":
           content = """<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Ping </title ></head >
           <body><h2> PING OK!</h2><p> The SEQ2 server in running.... </p><a href="/">Main page</a></body></html>"""
           cod = 200
       elif option == "/get":
           get_seq = arguments[1]
           seq = get_seq.split('?')
           name, seq_index = seq[0].split("=")
           seq_index = int(seq_index)
           seq = LIST_SEQ[seq_index]
           content = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Get </title ></head >
           <body><h2> Sequence number {seq_index}</h2><p> {seq} </p><a href="/">Main page</a></body></html>"""
           cod = 200
       elif option == "/gene":
           get_gene = arguments[1]
           couple = get_gene.split('?')
           name, gene = couple[0].split("=")
           seq = Seq()
           filename = FOLDER + gene + TXT
           seq = Seq(seq.read_fasta(filename))
           gene = str(seq)
           content = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Gene </title ></head>
           <body><h2> Gene: {gene}</h2><textarea readonly rows="20" cols="80"> {gene_seq} </textarea><br><br>
           <a href="/">Main page</a></body></html>"""
           cod = 200
       elif option == "/operation":
           operation = arguments[1]
           couple = operation.split('&')
           name_s, seq = couple[0].split("=")
           name_o, op = couple[1].split("=")
           seq = Seq(seq)
           if op == "comp":
               result = seq.complement()
           elif op == "rev":
               result = seq.reverse()
           else:
               l = seq.len()
               A_COUNTER = seq.count_base('A')
               C_COUNTER = seq.count_base('C')
               G_COUNTER= seq.count_base('G')
               T_COUNTER = seq.count_base('T')
               A_PER = 100 * A_COUNTER / l
               C_PER = 100 * C_COUNTER / l
               G_PER = 100 * G_COUNTER / l
               T_PER = 100 * T_COUNTER / l
               result = f"""<p>Total length: {l}</p><p>A: {A_COUNTER} ({A_PER}%)</p><p>G: {C_COUNTER} ({C_PER}%)
               </p><p>C: {G_COUNTER} ({G_PER}%)</p><p>T: {T_COUNTER} ({T_PER}%)</p>"""

           content = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Operation </title >
           </head ><body><h2> Sequence </h2><p>{seq}</p><h2> Operation: </h2><p>{op}</p><h2> Result: </h2><p>{result}
           </p><br><br><a href="/">Main page</a></body></html>"""
           cod = 200

        # Generating the response message
       self.send_response(cod)  # -- Status line: OK!

       # Define the content-type header:
       self.send_header('Content-Type', 'text/html')
       self.send_header('Content-Length', len(str.encode(content)))

       # The header is finished
       self.end_headers()

       # Send the response message
       self.wfile.write(str.encode(content))

       return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
   print("Serving at PORT", PORT)

   # -- Main loop: Attend the client. Whenever there is a new
   # -- client, the handler is called
   try:
       httpd.serve_forever()
   except KeyboardInterrupt:
       print("")
       print("Stoped by the user")
       httpd.server_close()
