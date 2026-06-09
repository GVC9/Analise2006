def imc(peso,altura):
    return peso/(altura*altura)

alt=float(input("Digite sua altura:"))
peso=float(input("Digite seu peso:"))
resultado=imc(peso,alt)
print(f"Seu IMC é: {resultado:.2f}")