idade=float(input("Você tem quantos anos?"))
sexo=input("Seu genero é Masculino? Se sim, digite SIM:")
if sexo=="SIM" and idade >= 18:
    print("Bem vindo as Forças Armadas!")
else:
    print("Não foi dessa vez.")