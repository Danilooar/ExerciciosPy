"""
    DE ACORDO COM A HORA, O PROGRAMA DEVE EXIBIR UMA MENSAGEM DE BOA TARDE, BOA NOITE OU BOM DIA.
    O PROGRAMA DEVE CONSIDERAR QUE O DIA COMEÇA ÀS 00:00 E TERMINA ÀS 23:59. 
    
 """


Hora = float(input("Digite a hora: "))

if Hora <= 12:
    print("Bom dia")
elif Hora <= 18:
    print("Boa tarde")
elif Hora > 18:
    print("Boa noite")