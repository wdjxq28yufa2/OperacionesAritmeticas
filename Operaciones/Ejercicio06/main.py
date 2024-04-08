from Suma import Suma
from Resta import Resta

if __name__ == '__main__':
    primerSumando = int(input("Ingrese el primer sumando: "))
    segundoSumando = int(input("Ingrese segundo sumando: "))
    suma = Suma()
    resta= Resta()
    print(f"{primerSumando} + {segundoSumando} = {suma.CalcularSuma(primerSumando, segundoSumando)}")
    print(f"{primerSumando} + {segundoSumando} = {resta.CalcularResta(primerSumando, segundoSumando)}")
