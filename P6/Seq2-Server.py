import http.server
import socketserver
from pathlib import Path
from Seq1 import Seq


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
GET_Seq = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA","AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA","CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT","CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA","AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]

FOLDER = 
txt = ".txt"


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""


        print(self.requestline)

        # Analize the request line
        req_line = self.requestline.split(' ')

        # Get the path. It always start with the / symbol
        path = req_line[1]

        # Read the arguments
        arguments = path.split('?')

        # Get the option. It is the first argument
        option = arguments[0]

        # -- Content type header
        # -- Both, the error and the main page are in HTML
        contents = Path('error.html').read_text()
        code = 404
        if option == "/":
            # Open the form1.html file
            # Read the index from the file
            contents = Path('form-4.html').read_text()
            code = 200
        elif option == "/ping":
            contents = """
                    <!DOCTYPE html>
                    <html lang = "en">
                    <head>
                    <meta charset = "utf-8" >
                      <title> PING </title >
                    </head >
                    <body>
                    <h2> PING OK!</h2>
                    <p> The SEQ2 server in running... </p>
                    <a href="/">Main page</a>
                    </body>
                    </html>
                    """
            code = 200
        elif option == "/get":
            # -- Get the argument to the right of the ? symbol
            pair1 = arguments[1]
            # -- Get all the pairs name = value
            pair2 = pair1.split('&')
            # -- Get the two elements: name and value
            name, value = pair2[0].split("=")
            n = int(value)

            # -- Get the sequence
            seq = GET_seq[n]

            # -- Generate the html code
            contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                  <title> GET </title >
                                </head >
                                <body>
                                <h2> Sequence number {n}</h2>
                                <p> {seq} </p>
                                <a href="/">Main page</a>
                                </body>
                                </html>
                                """
            code = 200
        elif option == "/gene":
            # -- Get the argument to the right of the ? symbol
            pair1 = arguments[1]
            # -- Get all the pairs name = value
            pair2 = pair1.split('&')
            # -- Get the two elements: name and value
            name, gene = pair2[0].split("=")

            s = Seq()
            FILENAME= FOLDER + "\\" + gene + txt
            s1= Seq(s.read_fasta(FILENAME))
            gene_str = str(s1)
            # -- Generate the html code
            contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                  <title> GENE </title >
                                </head >
                                <body>
                                <h2> Gene: {gene}</h2>
                                <textarea readonly rows="20" cols="80"> {gene_str} </textarea>
                                <br>
                                <br>
                                <a href="/">Main page</a>
                                </body>
                                </html>
                                """
            code = 200
        elif option == "/operation":
            # -- Get the argument to the right of the ? symbol
            pair1 = arguments[1]
            # -- Get all the pairs name = value
            pair2 = pair1.split('&')
            # -- Get the two elements: name and value
            name, seq = pair2[0].split("=")
            # -- Get the two elements of the operation
            name, op = pair2[1].split("=")

            # -- Create the sequence
            s = Seq(seq)

            if option2 == "comp":
                result = s.complement()
            elif option2 == "rev":
                result = s.reverse()
            else:
                len = s.len()
                count_A = s.count_base('A')
                percentage_a = "{:.1f}".format(100 * ca / sl)
                count_C = s.count_base('C')
                percentage_c = "{:.1f}".format(100 * cc / sl)
                count_G = s.count_base('G')
                percentage_g = "{:.1f}".format(100 * cg / sl)
                count_T = s.count_base('T')
                percentage_t = "{:.1f}".format(100 * ct / sl)

                result = f"""
                        <p>Total length: {sl}</p>
                        <p>A: {ca} ({pa}%)</p>
                        <p>C: {cc} ({pc}%)</p>
                        <p>G: {cg} ({pg}%)</p>
                        <p>T: {ct} ({pt}%)</p>"""

            contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                  <title> OPERATION </title >
                                </head >
                                <body>
                                <h2> Sequence </h2>
                                <p>{seq}</p>
                                <h2> Operation: </h2>
                                <p>{op}</p>
                                <h2> Result: </h2>
                                <p>{result}</p>
                                <br>
                                <br>
                                <a href="/">Main page</a>
                                </body>
                                </html>
                                """
            code = 200

            # Generating the response message
        self.send_response(code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

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
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
