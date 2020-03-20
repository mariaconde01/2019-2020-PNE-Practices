#Write a program that opens the dna.txt file
# calculates the total number of bases, and the number of the different bases

f = open("dna.txt", 'r')
file2 = f.read()
seq = file2.strip('\n')
f.close()

count = 0
count_A = 0
count_C = 0
count_T = 0
count_G = 0

for i in seq:
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