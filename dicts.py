# Una lista
mi_lista = ["a", "b", "c", "d"]
mi_set = {1, 2, 3, 4}

print(mi_lista)
print(type(mi_lista))

print(mi_set)
print(type(mi_set))

print(len(mi_lista))

mi_set.pop()
print(mi_set) 

mi_set.add("a")
print(mi_set) 

mi_set.add("a")
print(mi_set) 

mi_set.discard(7)
print(mi_set) 

print(mi_lista.count("b"))
