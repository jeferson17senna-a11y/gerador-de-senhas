#importar bibliotecas
import secrets


def gerar_senha():

    while True:

        try:
            #recebe a quantidade de caracteres que o usuário deseja para a senha
            pergunta = int(input("qual a quantidade de caracteres ?: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if pergunta < 8:
            print("A senha deve ter no mínimo 8 caracteres")
            continue

        elif pergunta > 64:
            print("A senha deve ter no máximo 64 caracteres")
            continue
        break

    #variável para armazenar a senha
    senha = ""
    
    #quantidade de caracteres restantes para completar a senha
    quantidade_restante = pergunta - 4

    #variável com os caracteres
    minisculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = "!@#$%&*"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #variáveis com caracteres obrigatórios
    senha += secrets.choice(minisculas)
    senha += secrets.choice(numeros)
    senha += secrets.choice(simbolos)
    senha += secrets.choice(maiusculas)

    #repete 8 vezes o processo de escolha aleatória de um caractere
    for i in range(quantidade_restante):
        #variável com a escolha aleatória de um caractere da variável caracters
        caractere = secrets.choice(numeros + simbolos + maiusculas + minisculas)
        #adicionando o caractere escolhido à senha
        senha += caractere

    #listar senha em uma lista
    senha = list(senha)
    #embaralha a senha para que os caracteres obrigatórios não fiquem sempre na mesma posição
    secrets.SystemRandom().shuffle(senha)
    #transforma a lista de volta em uma string
    senha = ''.join(senha)

    return senha


senha = gerar_senha()
print("Senha gerada: ", senha)