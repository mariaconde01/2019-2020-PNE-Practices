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

#main program
def print_seqs(seq_list):
    index = 0
    for element in seq_list:
        print(f"Sequence {index}: (Lenght {element.len()}) {element}")
        index+=1
seq_lists = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_lists)

def generate_seqs(patron, number):
seq_list1 = generate_seqs(" A ", 3)
seq_list2 = generate_seqs(" AC ", 5)

print(" List 1: ")
print_seqs(seq_list1)

print()
print(" List 2: ")


print_seqs(seq_list2)