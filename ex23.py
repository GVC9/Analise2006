#1)Desenvolva um código python que leia
#5 valores e mostre se eles são par
#ou impar

for i in range(5):
    # Lê o valor digitado pelo usuário e converte para número inteiro
    numero = int(input(f"Digite o {i+1}º valor: "))

    # Verifica se o resto da divisão por 2 é zero
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")
    print("-" * 20)  
