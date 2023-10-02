import math
from time import sleep

def calcular_vazao(area, intensidade_chuva):
    return area * intensidade_chuva

def calcular_diametro(vazao):
    diametro = math.sqrt((4 * vazao) / (math.pi * 9.81))
    return diametro

def main():
    print("Dimensionamento das Tubulações Pluviais Residenciais\n")

    # Entrada de dados
    area = float(input("Informe a área de captação (em metros quadrados): "))
    intensidade_chuva = 0.1

    # Cálculo da vazão
    vazao = calcular_vazao(area, intensidade_chuva)
    print("\nA vazão necessária é de %.2f litros por segundo.\n" % vazao)

    # Cálculo do diâmetro
    diametro = calcular_diametro(vazao)
    print("O diâmetro recomendado para a tubulação é de %.2f mm.\n" % diametro)

if __name__ == "__main__":
    main()


sleep(5)
