from seq0 import *

folder = "../SESSION-04/"
filename = ".txt"

gene_list =["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
base_list=["A", "C", "T", "G"]
print("-----| Exercise 8 |------")

for element in gene_list:  #elemento es U5,ADA..
    dna_seq = seq_read_fasta(folder + element + filename)
    print( "Gene", element, ":", "Most frequent Base:", processing_genes(dna_seq))

