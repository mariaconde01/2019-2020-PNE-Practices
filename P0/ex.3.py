from seq0 import *

folder = "../SESSION-04/"
filename = ".txt"

gene_list=["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print("-----| Exercise 3 |------")

for element in gene_list:
    dna_seq = seq_read_fasta(folder + element + filename)
    print( "Gene", element, "---> length:", seq_len(dna_seq))
