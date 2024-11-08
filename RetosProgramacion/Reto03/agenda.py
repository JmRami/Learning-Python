### Clase Agenda ### 
### Vamos a crear la clase Agenda con la variable interna datos. ### 
### datos es un diccionario con claves: nombre y telefono.### 
### Los metodos de las clases serán las operaciones y además 2 operaciones extra que son guardar a Excel y recuperar de Excel los datos.### 
### El constructor de la clase recupera los datos de la agenda del fichero Excel.### 


import pandas as pd

class Agenda:
    entradas_agenda = []
    nombre_fichero="agenda.xlsx"
    __df__=""
    
    def __init__(self):
        self.__cargar_datos__(self.nombre_fichero)
        
    def __del__(self):
        self.__guardar_datos__(self.nombre_fichero)
    
    def __cargar_datos__(self, nombre_fichero):
        try:
            __df__=pd.read_excel(nombre_fichero,usecols="A:B")
        except: 
            print(f"Se ha producido un error leyendo el fichero '{self.nombre_fichero}'.")
        finally:
            pass            
        
        self.entradas_agenda = __df__.values.tolist()
        pass
    
    def __guardar_datos__(self, nombre_fichero):
        try:
            __df__=pd.DataFrame(self.entradas_agenda, columns=["nombre","telefono"])
            __df__.to_excel(self.nombre_fichero, index=False)
        except Exception:
            print(f"Se ha producido un error escribiendo el fichero '{self.nombre_fichero}: {Exception.__name__}'.")  
        
            
    def __mostrar_lista__(self):
        print(self.entradas_agenda)
        
    def __añadir_contacto__(self,nombre,telefono):
        # comprobar si el contacto ya existe
        dict_agenda={sublista[0]: sublista[1] for sublista in self.entradas_agenda}
        if nombre not in dict_agenda:
            self.entradas_agenda.append([nombre,telefono])
            print(f"Se ha añadido el contacto '{nombre}' con el telefono '{telefono}'")
        else:
            print(f"Se ha producido un error añadiendo el nombre '{nombre}' porque ya existe.")  
    
            
    def __eliminar_contacto__(self, nombre):
        # comprobar si el contacto ya existe
        dict_agenda={sublista[0]: sublista[1] for sublista in self.entradas_agenda}
        if nombre in dict_agenda:
            dict_agenda.__delitem__(nombre)
            self.entradas_agenda = [[key, value] for key, value in dict_agenda.items()]
            print(f"Se ha elimnado el contacto '{nombre}'")
        else:
            print(f"Se ha producido un error al eliminar el nombre '{nombre}' porque no existe.")  
