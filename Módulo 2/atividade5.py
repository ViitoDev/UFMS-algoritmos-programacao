# Desafio
valor_cliente = float(input("Digite a quantidade de dinheiro que você tem: "))

um_real = 100
cinquenta_centavos = 50
vinte_e_cinco_centavos = 25
dez_centavos = 10
cinco_centavos = 5
um_centavo = 1

quantidade_um_real = int(valor_cliente // um_real)
valor_cliente = valor_cliente % um_real

quantidade_cinquenta_centavos = int(valor_cliente // cinquenta_centavos)
valor_cliente = valor_cliente % cinquenta_centavos

quantidade_vinte_e_cinco_centavos = int(valor_cliente // vinte_e_cinco_centavos)
valor_cliente = valor_cliente % vinte_e_cinco_centavos

quantidade_dez_centavos = int(valor_cliente // dez_centavos)
valor_cliente = valor_cliente % dez_centavos

quantidade_cinco_centavos = int(valor_cliente // cinco_centavos)
valor_cliente = valor_cliente % cinco_centavos

quantidade_um_centavo = int(valor_cliente // um_centavo)
valor_cliente = valor_cliente % um_centavo

print(f"\nQuantidade de moedas de 1 real: {quantidade_um_real}")
print(f"Quantidade de moedas de 50 centavos: {quantidade_cinquenta_centavos}")
print(f"Quantidade de moedas de 25 centavos: {quantidade_vinte_e_cinco_centavos}")
print(f"Quantidade de moedas de 10 centavos: {quantidade_dez_centavos}")
print(f"Quantidade de moedas de 5 centavos: {quantidade_cinco_centavos}")
print(f"Quantidade de moedas de 1 centavo: {quantidade_um_centavo}")