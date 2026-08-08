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


def senha_personalizada():

    print("gerador de senhas")
    #pergunta ao usuário se deseja incluir letras maiúsculas, minúsculas, números e símbolos na senha
    try:
        quantidade = int(input("quantos caracteres? : "))
    except ValueError:
        print("Por favor, digite um número válido.")
        return  
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    #variável para armazenar os caracteres permitidos
    caracteres = ""
    minisculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = "!@#$%&*"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if incluir_maiusculas:
        caracteres += maiusculas
    if incluir_numeros:
        caracteres += numeros
    if incluir_simbolos:
        caracteres += simbolos
    if incluir_minusculas:
        caracteres += minisculas
    if not caracteres:
        print("Você deve selecionar pelo menos um tipo de caractere.")
        return

    #variável para armazenar a senha
    senha = ""

    if quantidade < 8:
        print("A senha deve ter no mínimo 8 caracteres")
        return
    elif quantidade > 64:
        print("A senha deve ter no máximo 64 caracteres")
        return

    quantidade_obrigatoria = 0

    if incluir_maiusculas:
        senha += secrets.choice(maiusculas)
        quantidade_obrigatoria += 1
    if incluir_numeros:
        senha += secrets.choice(numeros)
        quantidade_obrigatoria += 1
    if incluir_simbolos:
        senha += secrets.choice(simbolos)
        quantidade_obrigatoria += 1
    if incluir_minusculas:
        senha += secrets.choice(minisculas)
        quantidade_obrigatoria += 1

    nova_quantidade = quantidade - quantidade_obrigatoria

    for i in range(nova_quantidade):
        #variável com a escolha aleatória de um caractere da variável caracters
        caractere = secrets.choice(caracteres)
        #adicionando o caractere escolhido à senha
        senha += caractere

    senha = list(senha)
    secrets.SystemRandom().shuffle(senha)
    senha = ''.join(senha)
    return senha

while True:
    print("Gerador de Senhas")
    print("1 - Gerar senha aleatória")
    print("2 - Gerar senha personalizada")
    print("3 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        senha_gerada = gerar_senha()
        print(f"Senha gerada: {senha_gerada}")
    elif escolha == "2":
        senha_personalizada_gerada = senha_personalizada()
        if senha_personalizada_gerada:
            print(f"Senha personalizada gerada: {senha_personalizada_gerada}")
    elif escolha == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")