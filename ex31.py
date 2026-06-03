numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 0
# O loop roda enquanto o índice 'i' for menor que o tamanho da lista
while i < len(numeros):
    n = numeros[i] # Pega o número na posição atual
    
    # Se o resto da divisão por 2 for diferente de 0, ele é ímpar
    if n % 2 != 0:
        print(f"O número {n} é ímpar.")
        
    i += 1 # Soma 1 ao índice para ir para o próximo número