from seq0 import *

folder = "../SESSION-04/"
filename = "U5.txt"

print("DNA file:", filename)
sequence= seq_read_fasta(folder + filename)
print("The first 20 bases are:","\n" , sequence[:20])

