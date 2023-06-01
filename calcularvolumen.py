from math import pi


def volumen_cubo(lado):
    volumen = lado ** 3
    return volumen


def volumen_prisma(lado, altura):
    base = lado ** 2
    volumen = base * altura
    return volumen


def volumen_piramide(lado, altura):
    base = lado ** 2
    volumen = (base * altura) / 3
    return volumen


def volumen_cilindro(radio, altura):
    base = pi * radio ** 2
    volumen = base * altura
    return volumen


def volumen_cono(radio, altura):
    base = (pi * radio ** 2) / 3
    volumen = base * altura
    return volumen


def volumen_esfera(radio):
    volumen = (4 / 3 * pi) * radio ** 3
    return volumen
