v1=int(input("Digite um valor:"))
v2=int(input("Agora, outro:"))
p=input("Quer saber o maior valor? Se sim, digite SIM:")
if p=="SIM":
  if v1 > v2:
    print(f"O maior número é o primeiro: {v1}")
  elif v2 > v1:
    print(f"O maior número é o segundo: {v2}")
  else:
    print("Os dois números são iguais!")