import cadenas as cd

# Concatenación
cad=cd.Cadenas()
print (cad.__concatenacion__("Hello ","World"))

# Repetir cadena
print (cad.__repetir__("Hi",18))

# longitud
print (cad.__longitud__(cad.__repetir__("Hi",18)))

# Acceso a caracteres
try:
    print(cad.__acceso_caracter__("Welcome",0))
    print(cad.__acceso_caracter__("Welcome",-1))
    print(cad.__acceso_caracter__("Welcome",99))
except Exception as ex:
    print(f"Error en la funcion de acceso a caracteres: {type(ex).__name__} ejecutando la linea ")

# Subcadenas
print(cad.__subcadena__("0123456",0,3))
print(cad.__subcadena__("0123456",0,99))
print(cad.__subcadena__("0123456",0,-3))
print(cad.__subcadena__("0123456",3,1)) # nulo
print(cad.__subcadena__("0123456",3,"A")) # Dispara excepcion

# Encontrar cadenas
print(cad.__encontrar_cadena__("Hello World Kernnigan", "Ker"))
print(cad.__encontrar_cadena__("Hello World Kernnigan", "aaa")) # Devuelve -1
print(cad.__encontrar_cadena__("Hello World Kernnigan", "")) # Devuelve 0
print(cad.__encontrar_cadena__("Hello World Kernnigan", "H")) # Devuelve 0
                               
# Concatenación
cad=cd.Cadenas()
print (cad.__concatenacion__("Hello ","World"))

# Repetir cadena
print (cad.__repetir__("Hi",18))

# longitud
print (cad.__longitud__(cad.__repetir__("Hi",18)))

# Acceso a caracteres
try:
    print(cad.__acceso_caracter__("Welcome",0))
    print(cad.__acceso_caracter__("Welcome",-1))
    print(cad.__acceso_caracter__("Welcome",99))
except Exception as ex:
    print (f"Error en la funcion de acceso a caracteres: {type(ex).__name__} ejecutando la linea ")

# Subcadenas
print(cad.__subcadena__("0123456",0,3))
print(cad.__subcadena__("0123456",0,99))
print(cad.__subcadena__("0123456",0,-3))
print(cad.__subcadena__("0123456",3,1)) # nulo
print(cad.__subcadena__("0123456",3,"A")) # Dispara excepcion

# Encontrar cadenas
print(cad.__encontrar_cadena__("Hello World Kernnigan", "Ker"))
print(cad.__encontrar_cadena__("Hello World Kernnigan", "aaa")) # Devuelve -1
print(cad.__encontrar_cadena__("Hello World Kernnigan", "")) # Devuelve 0
print(cad.__encontrar_cadena__("Hello World Kernnigan", "H")) # Devuelve 0

# Reemplazo de cadena
print(cad.__remplazar_cadena__("ABABABABABAB","A","B"))
print(cad.__remplazar_cadena__("ABABABABABAB","a","b")) # No hay cambios
print(cad.__remplazar_cadena__("ABABABABABAB","AB","")) 

# Dividir cadenas
lista=cad.__dividir_cadena__("Hello Word"," ") # Crear la list lista
print (lista)

lista=cad.__dividir_cadena__("Hello|Word","|")
print (lista)

#Unir elementos de una lista en una cadena
print (cad.__unir_cadenas__(["1", "2", "3" ]))

#cadena a Mayusculas
print (cad.__a_mayusculas__("hola mundo"))

#cadena a minusculas
print (cad.__a_minusculas__("HOLA MUNDO 123"))

#es numerico
print (cad.__es_numerico__("123456"))
print (cad.__es_alfabetico__("abcde"))

#es palindromo
print (cad.__es_palindromo__("radar"))

#es anagrama
print (cad.__es_anagrama__("roma", "amor"))

#es isograma
print (cad.__es_isograma__("murcielago")) 
print (cad.__es_isograma__("Mm")) # se ha pasado a upper para que no consiere 

print (set("Murcielago"))
