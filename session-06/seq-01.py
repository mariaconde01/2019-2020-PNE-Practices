
class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):   #Initialize the sequence with the value
                                    # passed as argument when creating the object
        self.strbases = strbases
        print("New sequence created!")   #strbases es el primer parametro que se imprime en s1 o s2 (objetos)


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def __len__(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

    def len(self):
        return len(self.strbases)  # --- Programa principal


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")           #la f significa formato en string
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")


class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases  #para que no solo devuelva la sequencia sino tambien el nombre del gen

# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")