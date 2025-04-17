"""
Descrição: Este programa lê uma temperatura em Celsius e informa se está frio, quente ou muito frio. 
    
"""



Temperatura = float(input("Digite a temperatura em Celsius: "))




if Temperatura <= 10:
    print("Está muito frio")
elif Temperatura <= 20:
    print("Está frio")
elif Temperatura > 22:
    print("Está quente")