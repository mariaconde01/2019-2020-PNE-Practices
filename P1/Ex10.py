from Seq1 import *

folder = "../session-04/"
filename = ".txt"

print("-----|Practice 1, Exercise 10|-----")

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
base_list = ["A", "C", "T", "G"]

for element in gene_list:  # elemento es U5,ADA..
    dna_file = folder + element + filename
    s = Seq()
    s1=Seq(s.read_fasta(dna_file))
    print("Gene", element, ":", "Most frequent Base:", s1.processing_genes(base_list))