def somar(a,b):
    return a+b
def subtrair (a,b):
    return a-b
def mult (a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        print ("Valor invalido.")
escolha=""
while escolha != "0":
    escolha = input("Digite uma opção: 1-Somar, 2-Subtrair, 3-Multiplicar, 4-Divisão.")
    num1=int(input("Digite o primeiro numero:"))
    num2=int(input("Digie o segundo numero"))
    if escolha=="1":
        x=somar(num1,num2)
    elif escolha=="2":
        x=subtrair(num1,num2)
    elif escolha=="3":
        x=mult(num1,num2)
    else:
        x=div(num1,num2)
    print (f"O resultado da operação é {x}")
else:
    print("Operação terminada")    

