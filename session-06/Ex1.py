class Seq:
    def __init__(self, strbases):
        for i in strbases:
            if i !="A" or i !="C"  or i !="G"  or i !="T":
                print("ERROR")
        self.strbases=strbases
    print("new sequence is created!")


PASS


# -- Main program
s1 = seq("AAACGTC")
s2 = seq("CCGTA")
