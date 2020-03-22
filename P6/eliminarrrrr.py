class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print("Testing....")

print("otro ejemplo")



class Seq:
    "" " Una clase para representar secuencias " ""

    def __init__(self,strbases):  # Inicialice la secuencia con el valor # pasado como argumento al crear el objeto
         self .strbases = strbases
         print ( "¡ Nueva secuencia creada! " )

    def __str__(self):
        # - Acabamos de devolver la cadena con la secuencia de retorno

        return self.strbases


    def len(self):
        return len(self.strbases)  # --- Programa principal


s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# - Imprimir los objetos print ( f " Secuencia 1: { s1 } " )
print(f"Sequence 1: {s1}")
print(f"Longitud:{s1.len()}")
print(f"Sequence 2: {s2}")
print(f"Longitud: { s2.len ()}")


print("otro ejer")

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass  #se utiliza cuando en un bloque de código no se quiere hacer nada
# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Gene: {g}")
print(f"  Length: {g.len()}")

print("otro ejemplo")

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        #se le añade otro parametro que en este caso es el nombre
        super().__init__(strbases)  #utilizamos esto para coger los cambios es decir string de la class seq
        self.name = name   #cambiamos valor a string
        print("New gene created")

# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Gene: {g}")

print("OTRO EJERCICIO NUEVO:Overriding the Seq methods ")

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