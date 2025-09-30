import numpy as np
class Pila:
    __items:np.ndarray
    __tope:int
    __cant:int

    def __init__(self,cant):
        self.__cant = cant
        self.__tope = -1
        self.__items = np.empty(self.__cant,dtype=int)
    
    def insertar(self,x):
        if self.__tope < self.__cant-1:
            self.__tope += 1
            self.__items[self.__tope] = x
            retorno = x
        else:
            print('Pila llena')
            retorno = 0
        return retorno
    def vacia(self):
        return (self.__tope == -1)
    
    def suprimir(self):
        x = 0
        if self.vacia():
            print('Pila Vacia')
        else:
            x = self.__items[self.__tope]
            self.__tope -= 1
            resultado = x
        return resultado

    def mostrar(self):
        if not self.vacia():
            for i in range(self.__tope, -1, -1):
                print(f'Posicion {i} valor{self.__items[i]}')
        else:
            print('Pila vacia')