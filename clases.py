class Operaciones:
    def __init__(self, operando1, operando2):
        self.__oper1=operando1
        self.__oper2=operando2
        self.param_visible=""
        
    def suma(self):
        return self.__oper1+self.__oper2
    
    def division(self):
        try:
            resultado= self.__oper1/self.__oper2
        except Exception as e:
            #return f"Error: {type(e).__name__}"
            return f"Error: {e}"
        else:
            return resultado
        finally:
            print ("Fin de programa")
