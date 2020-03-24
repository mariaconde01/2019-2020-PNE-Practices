from Seq1 import Seq

print("-----|Practice 1, Exercise 9|-----")

folder = "../Session-04/"
filename ="U5.txt"
FILENAME=folder+filename
s = Seq()
s1 = Seq(s.read_fasta(FILENAME))

print("Sequence 1", ": (Length:",  s1.len(), ")", (s1))
print(f"Bases: {s1.count()}")
print(f"Reverse: {s1.reverse()}")
print(f"Comp: {s1.complement()}")