from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

body = file_contents.split("\n")[1:]
string =""
string =("\n").join(body).replace("","") #("\n") en vez de string para hacer que no este tod en 1 sola linea

print("Body of the ud.txt file :\n",string)
