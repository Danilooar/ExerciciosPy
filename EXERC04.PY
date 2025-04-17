
'''
GERADOR DE LOGIN E SENHA
O programa deve solicitar ao usuário um nome de usuário e uma senha. 
Após isso, o programa deve solicitar o nome de usuário e a senha novamente. 
Caso o usuário e a senha estejam corretos, o programa deve exibir uma mensagem de boas-vindas. 
Caso contrário, o programa deve exibir uma mensagem de erro.
'''


Usuario_1 = 'admin'
Usuario_1_senha = "123456"

user = input("Digite o usuario: ")

senha = input("Digite a senha: ")

if user == Usuario_1 and senha == Usuario_1_senha:
    print("Usuario e senha corretos")
else:
    print("Usuario ou senha incorretos")
    print("Acesso negado")
    
    