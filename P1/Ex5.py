from Seq1 import *

print("-----| Practice 1, Exercise 5 |------")

# - Crear una secuencia nula
s0 = Seq ()

# - Crear una secuencia válida
s1 = Seq("ACTGA")

# - Crear una secuencia inválida
s2 = Seq ("INVALID SEQUENCE " )

# - crear lista con bases correctas
list_base = ["A", "C", "T", "G"]

# -- Printing the objects

print(f"\nSequence 0: (Length: {s0.len()}) {s0}")
for base in list_base:
    print(base, ":", s0.count_base(base), end=" ,")

print(f"\nSequence 1: (Length: {s1.len()}) {s1}")
for base in list_base:
    print(base, ":", s1.count_base(base), end=" ,")

print(f"\nSequence 2: (Length: {s2.len()}) {s2}")
for base in list_base:
    print(base, ":", s2.count_base(base), end=" ,")