from Calculararea import *
from calcularvolumen import *

if __name__ == '__main__':
    print(__name__)
    lado = int(input("Introduzca lado: "))
    print("Área del cuadrado: ", area_cuadrado(lado))

    radio = int(input("Introduzca el radio del círculo: "))
    print("Área del círculo: ", area_circulo(radio))

    print("Volumen de la esfera: ", volumen_esfera(radio))

    print("Área del Rombo: ", area_rombo(25, 50))
