### Clase Agenda ### 
### Vamos a crear la clase Agenda con la variable interna datos. ### 
### datos es un diccionario con claves: nombre y telefono.### 
### Los metodos de las clases serán las operaciones y además 2 operaciones extra que son guardar a Excel y recuperar de Excel los datos.### 
### El constructor de la clase recupera los datos de la agenda del fichero Excel.### 

import pandas as pd

class Agenda:
    datos = {}
    nombre_fichero="agenda.xlsx"
    
    def __init__(self):
        self.__cargar_datos__(self.nombre_fichero)
    
    
    def __cargar_datos__(self, nombre_fichero):
        try:
            fd=pd.read_excel(nombre_fichero,usecols="A:B")
        except: 
            print(f"Se ha producido un error leyendo el fichero '{nombre_fichero}'.")
        finally:
            pass
        print(fd)
            
a=Agenda()    