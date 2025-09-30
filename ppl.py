from clase_pila import Pila

def test():
    dimension = int(input('Items->'))
    P = Pila(dimension)
    numero = int(input('Numero->'))
    print(P.insertar(numero))
    numero = int(input('Numero->'))
    print(P.insertar(numero))
    numero = int(input('Numero->'))
    print(P.insertar(numero))
    print(P.suprimir())
    P.mostrar()


if __name__ == '__main__':
    test()