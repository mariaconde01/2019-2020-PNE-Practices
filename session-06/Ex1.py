class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        good = True
        for i in strbases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                good = False

        if good == True:
            self.strbases = strbases
            print("New sequence created!")

        else:
            strbases = "ERROR"
            self.strbases = strbases
            print("ERROR!!")

    def __str__(self):
        return self.strbases


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
