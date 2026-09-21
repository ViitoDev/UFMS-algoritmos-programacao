tempo = float(input("Digite o tempo (em segundos) entre ver o raio e ouvir o trovão: "))
velocidade_som = 340
distancia_metros = velocidade_som * tempo
distancia_km = distancia_metros / 1000

print(f"\nA distância aproximada do raio é: {distancia_metros:.2f} metros")