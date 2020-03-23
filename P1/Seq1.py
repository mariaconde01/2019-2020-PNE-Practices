class Seq:
    NULL = "NULL"
    ERROR = "ERROR"
    def __init__(self, strbases= "NULL"):
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL sequence created!")
            return
        good=True
        for i in strbases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                self.strbases = "ERROR"
                good=False
                print("INVALID Seq!")
                return

            else:
                self.strbases = strbases
                print("New sequence created!")
                return

    def __str__(self):
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        counter=0
        if self.strbases == self.NULL:
            return 0

        elif self.strbases==self.ERROR:
            return 0
        else:
            counter +=1
            return len(self.strbases)

    def count_base(self, base):
            counter = 0
            if self.strbases == self.NULL:
                return counter
            elif self.strbases == self.ERROR:
                return counter
            else:
                for character in self.strbases:
                    if character == base:
                        counter += 1
                return counter


