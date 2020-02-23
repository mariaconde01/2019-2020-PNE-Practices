class seq:
    """a class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")
    def __str__ (self):
        return self.strbases
    def len(self):
        return len(self.strbases)




    pass

class Gene(seq):
    pass

# -- Main program
s1=seq("AAACGTC")
g= Gene("ACCTGA")
print(f"sequence 1: {s1}") #la f significa formato en string
print(f"sequence 2: {g}")

print(f"The length of the sequence 1 is {s1.len()}")
print(f"The length of the sequence 2 is {g.len()}")
