from Seq1 import *

print("-----| Practice 1, Exercise 4 |------")

# - Crear una secuencia nula
s1 = Seq ()

# - Crear una secuencia válida
s2 = Seq("ACTGA")

# - Crear una secuencia inválida
s3 = Seq ("INVALID SEQUENCE " )

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
print(f"Sequence 3: {s3}")

print(f"Sequence 1: (length: {s1.len()}) {s1}")
print(f"Sequence 2: (length: {s2.len()}) {s2}")
print(f"Sequence 3: (length: {s3.len()}) {s3}")