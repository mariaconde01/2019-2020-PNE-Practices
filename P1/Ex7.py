from Seq1 import *

print("-----| Practice 1, Exercise 7 |------")

# - Crear una secuencia nula
s0 = Seq ()

# - Crear una secuencia válida
s1 = Seq("ACTGA")

# - Crear una secuencia inválida
s2 = Seq ("INVALID SEQUENCE " )

# - crear lista con bases correctas
list_base = ["A", "T", "C", "G"]

print(f"Sequence 0: (length: {s0.len()}) {s0}")
print(f"Bases:", s0.count())
print(f"Rev: {s0.reverse()}")

print(f"Sequence 1: (length: {s1.len()}) {s1}")
print(f"Bases:", s1.count())
print(f"Rev: {s1.reverse()}")

print(f"Sequence 2: (length: {s2.len()}) {s2}")
print(f"Bases:", s2.count())
print(f"Rev: {s2.reverse()}")



