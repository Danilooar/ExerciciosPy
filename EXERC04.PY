Usuario_1 = 'admin'
Usuario_1_senha = "123456"

user = input("Digite o usuario: ")

senha = input("Digite a senha: ")

if user == Usuario_1 and senha == Usuario_1_senha:
    print("Usuario e senha corretos")
else:
    print("Usuario ou senha incorretos")
    print("Acesso negado")
    
    