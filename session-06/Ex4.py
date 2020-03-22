import termcolor

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
def print_seqs(seq_list, colour):
    index = 0
    for element in seq_list:
        termcolor.cprint(f"Sequence {index}: (Lenght {element.len()}) {element}")
        index+=1