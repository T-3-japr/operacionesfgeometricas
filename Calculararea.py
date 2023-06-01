import math
# Funciones para cálculo del área de figuras geométricas


def area_cuadrado(lado):
    try:
        a_cuadrado = lado ** 2
    except TypeError:
        print("El valor debe ser numérico")
        a_cuadrado = 0
    return a_cuadrado


def area_triangulo(base, altura):
    a_triangulo = (base * altura) / 2
    return a_triangulo


def area_circulo(radio):
    a_circulo = math.pi*radio ** 2
    return a_circulo


def area_rectangulo(base, altura):
    a_rectangulo = base * altura
    return a_rectangulo


def area_trapecio(Base, altura, base):
    a_trapecio = ((Base + base) / 2) * altura
    return a_trapecio


def area_paralelogramo(base, altura):
    a_triangulo = (base * altura) / 2
    return a_triangulo


def area_poligono_regular(n_lados, lado, apotema):
    a_poligono = ((n_lados * lado) * apotema) / 2
    return a_poligono


def area_rombo(DiagonalM, diagonalm):
    a_rombo = (DiagonalM * diagonalm) / 2
    return a_rombo

