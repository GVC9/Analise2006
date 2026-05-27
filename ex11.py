anoN=float(input("Digite o ano do seu nascimento:"))
anoA=float(input("Qual é o ano atual?"))
idade=anoA-anoN
if idade >= 18:
    print(f"Você tem {idade} anos, é maior de idade!")    
else:
    print(f"Você tem {idade} anos, é menor de idade!") 
