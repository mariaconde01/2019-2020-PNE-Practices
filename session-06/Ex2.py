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

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list):
    index = 0
    for element in seq_list:
        print(f"Sequence {index}: (Length: {element.len()}) {element}")
        index += 1

seq_lists = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_lists)

