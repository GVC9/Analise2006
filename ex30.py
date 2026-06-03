numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 0
# O loop roda enquanto 'i' for menor que o tamanho da lista
while i < len(numeros):
    n = numeros[i] # Pega o número na posição atual
    
    if n % 2 == 0:
        print(f"O número {n} é par.")
        
    i += 1 # Avança para o próximo índice (evita o loop infinito)