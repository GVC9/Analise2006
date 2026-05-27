v=float(input("Digite um valor:"))
p = float(input("Agora, uma porcentagem: ").replace('%', '').replace(',', '.'))
total=v*p/100
print(f"A porcetagem de {p}% do valor {v} é de {total}")