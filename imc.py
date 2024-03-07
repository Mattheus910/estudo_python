print('Calculo de IMC')
print('______________')

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite o sua altura: "))
imc = peso / (altura * altura)

def calculoImc(imc):
    match imc:
        case (imc<=18.5)
            print('')

