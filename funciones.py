def sum(lista=[5, 6, 7]):
    if type(lista)!=list:
        return "error de parametro"
    
    ### devuelve la suma de una lista
    res=0
    for i in lista:
        if i==3:
            break
        else:
            res+=i
    return res

print(sum([1, 2, 3]))
print(sum(2))
print(sum())

def sum_param_arbitrarios(*enteros:int):
    res=0
    for i in enteros:
        res += i
    return res

print(sum_param_arbitrarios(1, 7, 8, 12, 1.1))

from clases import Operaciones
    
suma = Operaciones(3, 4).suma()
print(f"el resultado de la suma de 3 + 4 es {suma}")
print(suma)
print(Operaciones(3,5).param_visible)

division=Operaciones(3,0).division()
print(division)
    
import pandas
pandas