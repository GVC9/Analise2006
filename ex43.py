def imposto(sal,imp):
    return imp*sal

sal=float(input("Digite seu salário:"))
imp=0.275
resultado=imposto(sal,imp)
print(f"Seu imposto de renda é de: {resultado:.2f}")