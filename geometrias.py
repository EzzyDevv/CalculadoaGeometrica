from math import ceil

print("-" * 25)
def retangulo(base_retangulo, altura_retangulo):
    area_retangulo = base_retangulo * altura_retangulo
    perimetro_retangulo = 2 * (base_retangulo + altura_retangulo)
    print("Área do retângulo : {:.2f}\nPerímetro do retângulo : {:.2f}.".format(area_retangulo, perimetro_retangulo))


def triangulo(base_triangulo, altura_triangulo, ladoA_triangulo, ladoB_triangulo, ladoC_triangulo):
    area_triangulo = (base_triangulo * altura_triangulo) / 2
    perimetro_triangulo = ladoA_triangulo + ladoB_triangulo + ladoC_triangulo
    print("Área do triângulo : {:.2f}\nPerímetro do triângulo : {:.2f}".format(area_triangulo, ceil(perimetro_triangulo)))


def circulo(diametro_circulo):
    raio = diametro_circulo / 2
    area_circulo = (3.14159265 * raio) ** 2
    perimetro_circulo = 2 * 3.14159265 * raio
    print("Área do círculo : {:.2f}\nPerímetro do círculo : {:.2f}".format(area_circulo, ceil(perimetro_circulo)))