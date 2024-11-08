# Pilas

# Lista como pila
pila = [1, 2, 3, 4]
# Añadir un elemento
pila.append(5)
print(pila)

# leer un elemento
pila.pop()
print(pila)

# Lista como cola
cola = [1, 2, 3, 4]

# añadir elemento
cola.insert(0, 0)
print(cola)

# leer un elemento
cola.pop()
print(cola)

#Simulación de navegador

import webbrowser

pila_urls=["https://wwww.microsoft.com", "https://www.google.com", "https://www.apple.com"]
indice = 2
opcion=0
while opcion!="4":
    opcion=input("Opciones: (1) Entrar URL, (2) Atras, (3) Adelante, (4) Salir: ")
    if opcion == "1":
        url=input("URL: ")
        pila_urls.append(url)
        indice+=1
    elif opcion == "2":
        indice-=1
        url=pila_urls[indice]
    elif opcion == "3":
        if indice==len(pila_urls)-1:
            print("no hay mas URLs")
        else:
            indice+=1
            url=pila_urls[indice]
    elif opcion == "4":
        pass

    webbrowser.open(url)
        