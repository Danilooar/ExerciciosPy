Hora = float(input("Digite a hora: "))

if Hora <= 12:
    print("Bom dia")
elif Hora <= 18:
    print("Boa tarde")
elif Hora > 18:
    print("Boa noite")