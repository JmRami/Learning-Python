# Recursividad

def descontar(numero):
    if numero <= 0:
        return
    else:
        print(numero)
        descontar(numero - 1)
        
        
# descontar(100)

# Factorial

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero -1)

print (factorial(3))    

i=1

# Fibonnaci

def fib(num, valor):
    lista_fib=[1, 2]
    while num>=0:
        lista_fib.append(lista_fib[-1] + lista_fib[-2])
        num-=1
        if lista_fib[-1]==valor:
            return([lista_fib.__len__(), lista_fib])
    return(lista_fib)
    
print(fib(20, 8))
        
    
    
        