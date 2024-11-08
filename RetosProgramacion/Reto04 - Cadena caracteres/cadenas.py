class Cadenas:
    
    def __init__(self):
        pass

    def __concatenacion__(self, cadena1, cadena2): 
        return(cadena1+cadena2)
    
    def __repetir__(self, cadena, veces):
        return(cadena*veces)
    
    def __longitud__(self,cadena):
        return(len(cadena))
    
    def __acceso_caracter__(self,cadena,numero_caracter):
        return(cadena[numero_caracter])
    
    def __subcadena__(self,cadena,caracter_inicial, caracter_final):
        try:
            return(cadena[caracter_inicial:caracter_final])
        except Exception as ex:
            print (f"Error en subcadena: {type(ex).__name__}")
    
    def __encontrar_cadena__(self, cadena_completa, cadena_buscada):
        return(cadena_completa.find(cadena_buscada))
    
    def __remplazar_cadena__(self,cadena_original, cadena_buscada, remplazo):
        return(cadena_original.replace(cadena_buscada, remplazo))
    
    def  __dividir_cadena__(self,cadena,separador):
        return(cadena.split(separador))
    
    def __unir_cadenas__(self, lista):
        return("".join(lista))
    
        