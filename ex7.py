nome=input("Qual o seu nome?")
alt=float(input("Qual a sua altura?"))
peso=float(input("E seu peso atual?"))
input(f"Gostaria de saber seu IMC? Prezado,{nome}?")
if "Sim":
    IMC=peso/(alt*alt)
print(f"{nome}, seu IMC é de: {IMC}")