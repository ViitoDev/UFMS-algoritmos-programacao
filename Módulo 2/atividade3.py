import math

x1 = float(input("Digite a coordenada x1: "))
y1 = float(input("Digite a coordenada y1: "))
x2 = float(input("Digite a coordenada x2: "))
y2 = float(input("Digite a coordenada y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"\nA distância entre os pontos A({x1}, {y1}) e B({x2}, {y2}) é: {distancia:.2f}")