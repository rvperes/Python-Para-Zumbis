ladoa = float(input("Lado A: "))
ladob = float(input("Lado B: "))
ladoc = float(input("Lado C: "))
if ladoa < (ladob+ladoc) and ladob < (ladoa + ladoc) and ladoc < (ladoa + ladob):
    print("O triangulo existe!")
    triangulo = "existe"
else:
    print("O triangulo não existe!")
    triangulo = "naoexiste"
if triangulo == "existe":
    if ladoa == ladob and ladoa == ladoc and ladob == ladoc:
        print("Este triangulo é equilátero!")
    elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
        print("Este triangulo é isosceles!")
    else:
        print("Este triangulo é escaleno!")