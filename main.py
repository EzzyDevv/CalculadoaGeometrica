import geometrias


formula = int(input("""Escolha a forma : \n1 - Retângulo\n2 - Triângulo\n3 - Círculo\n>>> """))

match formula:
    case 1:
        base = float(input("Digite a base do retângulo : "))
        altura = float(input("Digite a altura do retângulo : "))
        geometrias.retangulo(base, altura)
    case 2:
        base = float(input("Digite a base do triângulo : "))
        altura = float(input("Digite a altura do triângulo : "))
        lado_a = float(input("Digite o lado A do triângulo : "))
        lado_b = float(input("Digite o lado B do trângulo : "))
        lado_c = float(input("Digite o lado C do triângulo : "))
        geometrias.triangulo(base, altura, lado_a, lado_b, lado_c)
    case 3:
        diametro = float(input("Digite o diâmetro do círculo : "))
        geometrias.circulo(diametro)