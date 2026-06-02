valor=int(input("Digite um valor:"))
print(f"--- Tabuada do {valor} ---")
i=1
while i <= 10:
    resultado = valor * i
    print(f"{valor} x {i} = {resultado}")
    i = i + 1