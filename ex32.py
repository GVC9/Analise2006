x = 1          # Começamos o contador em 1
soma = 0       # Essa variável vai guardar o total da soma

while x <= 100:
    soma = soma + x  # Adiciona o valor atual de x ao total
    x = x + 1        # Avança para o próximo número

print(f"A soma dos números de 1 a 100 é: {soma}")