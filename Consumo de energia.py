consumo = float(input("Digite a quantidade de Kwh consumida: "))
tipo = input ("Qual o tipo de Instalação, Residencia, Industria, Comercio: ")
if (tipo == "R"):
    if (consumo <= 500):
        valor = consumo * 0.40
        print (valor)
    elif (consumo > 500):
        valor = consumo * 0.65
        print (valor)
if (tipo == "C"):
    if (consumo <= 1000):
        valor = consumo * 0.55
        print (valor)
    elif (consumo > 1000):
        valor = (consumo * 0.60)
        print (valor)
if (tipo == "I"):
    if (consumo <= 5000):
        valor = consumo * 0.55
        print (valor)
    elif (consumo > 5000):
        valor = (consumo * 0.60)
        print (valor)