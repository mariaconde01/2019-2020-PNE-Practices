from seq0 import *

folder = "../SESSION-04/"
filename = "U5.txt"

print("-----| Exercise 7 |------")

print("Gene U5:")
sequence= seq_read_fasta(folder + filename)
print("Frag:", seq_read_fasta(folder+ filename)[:20])
print("Comp:", seq_complement(seq_read_fasta(folder + filename)[:20]))