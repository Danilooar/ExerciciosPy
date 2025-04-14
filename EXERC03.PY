Valor_Compra = float(input( "Digite o valor da compra: "))

if Valor_Compra > 10:
    Desconto = Valor_Compra * 0.05
    Valor_Final = Valor_Compra - Desconto
    print("Valor do desconto: ", Desconto)
    print("Valor a pagar: ", Valor_Final)

elif Valor_Compra > 100:
    Desconto = Valor_Compra * 0.1
    Valor_Final = Valor_Compra - Desconto
    print("Valor do desconto: ", Desconto)
    print("Valor a pagar: ", Valor_Final)
    
elif Valor_Compra > 200:
    Desconto = Valor_Compra * 0.2
    Valor_Final = Valor_Compra - Desconto
    print("Valor do desconto: ", Desconto)
    print("Valor a pagar: ", Valor_Final)