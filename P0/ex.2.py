from seq0 import *

FOLDER = "../SESSION-04/"
FILENAME = "U5.txt"

seq_dna = Seq0.seq_read_fasta(FOLDER + FILENAME)[0:20]
print("DNA file:", FILENAME)
print("The first 20 DNA bases are:", seq_dna)