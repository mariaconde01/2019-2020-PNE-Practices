from Seq1 import *

print("-----| Practice 1, Exercise 6 |------")

# - Crear una secuencia nula
s0 = Seq ()

# - Crear una secuencia válida
s1 = Seq("ACTGA")

# - Crear una secuencia inválida
s2 = Seq ("INVALID SEQUENCE " )

# - crear lista con bases correctas
list_base = ["A", "T", "C", "G"]

print(f"Sequence 0: (Length: {s0.len()}) {s0}")
print("Bases:", s0.count())

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print("Bases:", s1.count())

print(f"Sequence 2: Length: {s2.len()}) {s2}")
print("Bases:", s2.count())