from datetime import datetime

# 1. Recebe o dia da semana
diasemana = input("Qual o dia da semana? ").lower().strip()

# 2. Valida o horário de forma segura
while True:
    entrada = input("Que horas acaba a aula? (Formato 24h - HH:MM): ").strip()
    
    try:
        # GARANTA QUE ESSA LINHA NÃO TEM PONTO FINAL DENTRO DAS ASPAS:
        horario_validado = datetime.strptime(entrada, "%H:%M")
        print(f"Horário aceito com sucesso: {horario_validado.strftime('%H:%M')}.\n")
        break  # Sai do loop imediatamente se der certo
    except ValueError:
        print("Horário inválido! Certifique-se de usar o formato de 24h (00:00 até 23:59).\n")

# 3. Extrai apenas a hora (como número inteiro)
hora = horario_validado.hour

# 4. Condicionais de recompensa
if diasemana == "sexta":
    if hora >= 22:
        print("Sextou pesado! Você ralou até tarde e merece pelo menos 2 chopps!")
    elif hora >= 21:
        print("Sextou! A aula acabou e você merece 1 chopp da sua preferência.")
    else:
        print("Ainda é cedo na sexta! A aula não acabou, continue focado!")
else:
    print("Ainda não Sextou! Continue estudando!")