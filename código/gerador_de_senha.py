#importar bibliotecas
import secrets

#variável para armazenar a senha
senha = ""

#variável com os caracteres
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*"

#recebe a quantidade de caracteres que o usuário deseja para a senha
pergunta = int(input("qual a quantidade de caracteres ?: "))

if pergunta < 8:
    print("A senha deve ter no mínimo 8 caracteres")

elif pergunta > 64:
    print("A senha deve ter no máximo 64 caracteres")

else:
    #repete 8 vezes o processo de escolha aleatória de um caractere
    for i in range(pergunta):
        #variável com a escolha aleatória de um caractere da variável caracters
        gerar_senha = secrets.choice(letras + numeros + simbolos)
        #adicionando o caractere escolhido à senha
        senha += gerar_senha

    print(senha)