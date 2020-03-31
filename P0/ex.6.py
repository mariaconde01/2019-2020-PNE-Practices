from seq0 import *

folder = "../SESSION-04/"
filename = "U5.txt"

print("-----| Exercise 6 |------")

print("Gene U5:")
print("Frag:", seq_read_fasta(folder+ filename)[:20])
print("Rev:", seq_reverse(seq_read_fasta(folder + filename)[:20]))