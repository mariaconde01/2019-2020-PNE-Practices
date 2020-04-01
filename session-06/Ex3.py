class Seq:

    """A class for representing sequence objects"""
    def __init__(self, strbases):
        good = True
        for i in strbases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                good = False
                print("ERROR")

        if good == True:
            self.strbases = strbases
            print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list):
    index = 0
    for element in seq_list:
        print(f"Sequence {index}: (Length: {element.len()}) {element}")
        index += 1

def generate_seqs(pattern, number):
    list=[]
    for element in range(1, number+1):
        sequence=pattern*element
        list.append(Seq(sequence))
    return list

#main program
seq_list1 = generate_seqs("A",3)
seq_list2 = generate_seqs("AC",5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)