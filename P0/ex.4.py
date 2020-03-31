from seq0 import *

folder = "../SESSION-04/"
filename = ".txt"

gene_list=["U5","ADA", "FRAT1", "FXN", "RNU6_269P"]
base_list=["A", "C", "T", "G"]
print("-----| Exercise 4 |------")

for element in gene_list:
    dna_seq = seq_read_fasta(folder + element + filename)
    print( "Gene", element)

    for base in base_list:
        print(base, ":", seq_count_base(dna_seq, base))