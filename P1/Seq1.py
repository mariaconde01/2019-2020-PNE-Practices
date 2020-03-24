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

    def count(self):

        bases = ["A", "T", "C", "G"]
        count_bases = []
        for element in bases:
            count_bases.append(self.count_base(element))
        dictionary = dict(zip(bases, count_bases))
        return dictionary

    def reverse(self):

       if self.strbases==self.NULL:
           return("NULL")
       elif self.strbases == self.ERROR:
           return("ERROR")
       else:
           return self.strbases[::-1]

    def complement(self):

        bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comp_bases = ""

        if self.strbases == self.NULL:
            return ("NULL")
        elif self.strbases == self.ERROR:
            return ("ERROR")
        else:
            for element in self.strbases:
                comp_bases += bases[element]
            return comp_bases

    def read_fasta(self, filename):
        from pathlib import Path
        string=""
        file_contents = Path(filename).read_text()
        files = file_contents.split('\n')
        body=files[1:]
        string=string.join(body).replace(" ", "")  #pasas el body a string y lo
        return (string)                            #el valor se tiene que devolver en forma de string



    def processing_genes(self):
        dict_base = seq_count(seq)
        max_base = max(dict_base, key=dict_base.get)  # la funcion get te encuentra la base mas frecuente
        return max_base



