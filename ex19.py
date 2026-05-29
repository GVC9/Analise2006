# 1. Recebe e padroniza o cargo
cargo = input("Qual o seu cargo? ").lower().strip()

# 2. Define o Salário Bruto baseado no cargo
salario_bruto = 0.0  # Começa com zero caso o cargo não exista

if cargo == "caixa":
    salario_bruto = 1500.00
elif cargo == "vendedor":
    salario_bruto = 2400.00
elif cargo == "gerente":
    salario_bruto = 4000.00
else:
    print("Cargo inválido. Não trabalha aqui.")

# 3. Se o cargo for válido (salário maior que zero), faz os cálculos
if salario_bruto > 0:
    
    # Cálculo do INSS (Fixo 12% para todos)
    desconto_inss = salario_bruto * 0.12
    
    # Cálculo do IRRF (Alíquota variável)
    if salario_bruto > 2000.00:
        desconto_irrf = salario_bruto * 0.14  # 14% para maiores que 2k
    else:
        desconto_irrf = salario_bruto * 0.08  # 8% para menores ou iguais a 2k
        
    # Cálculo do Salário Líquido
    salario_liquido = salario_bruto - desconto_inss - desconto_irrf
    
    # 4. Saída de dados formatada
    print("\n" + "="*30)
    print(f"RESUMO DA FOLHA - CARGO: {cargo.upper()}")
    print("="*30)
    print(f"Salário Bruto Inicial: R$ {salario_bruto:,.2f}")
    print(f"(-) Desconto INSS (12%): R$ {desconto_inss:,.2f}")
    
    # Mostra a porcentagem real aplicada no IRRF para ficar claro
    porcentagem_irrf = "14%" if salario_bruto > 2000 else "8%"
    print(f"(-) Desconto IRRF ({porcentagem_irrf}): R$ {desconto_irrf:,.2f}")
    
    print("-"*30)
    print(f"Salário Líquido Final: R$ {salario_liquido:,.2f}")
    print("="*30)