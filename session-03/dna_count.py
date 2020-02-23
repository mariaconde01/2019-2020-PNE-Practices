# Create a program for counting the number of bases presented in a DNA sequence.
# The user introduces a sequence of letter representing the DNA chain.
# Our program should calculate the total length, and the number of bases that compound the sequence.

dna_seq = input("Introduce the sequence:")

count = 0

count_A = 0
count_C = 0
count_T = 0
count_G = 0

for i in dna_seq:
    count += 1
    if i == "A":
        count_A += 1
    elif i == "C":
        count_C += 1
    elif i == "T":
        count_T += 1
    else:
        count_G += 1

print("Total length: ", count)
print("A: ", count_A)
print("C: ", count_C)
print("T: ", count_T)
print("G: ", count_G)
