#liquidacao de loja

P=float(input("Preco do produto: "))
D=float(input("Desconto (em %): "))
print(f"Valor original: {P}\nDesconto: {(P*D)/100}\nNovo valor: {P-(P*D)/100}")
