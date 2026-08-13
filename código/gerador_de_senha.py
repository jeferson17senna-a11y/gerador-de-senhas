#importar bibliotecas
import secrets
import json

def menu():
    print('''
--- Gerador de Senhas ---
1 - Gerar senha aleatória
2 - Gerar senha personalizada
3 - Verificar força da senha
4 - consultar senhas salvas
5 - guardar senhas já criadas
6 - excluir senha existente
7 - alterar senha/usuario/site
8 - sair''')


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


def verificar_forca_senha(senha):

    tem_minusculas = False
    tem_maiusculas = False
    tem_numeros = False
    tem_simbolos = False

    for caractere in senha:
        if caractere.islower():
            tem_minusculas = True
        if caractere.isupper():
            tem_maiusculas = True
        if caractere.isdigit():
            tem_numeros = True
        if not caractere.isalnum():
            tem_simbolos = True

    pontuacao = 0

    if tem_minusculas:
        pontuacao += 1
    if tem_maiusculas:
        pontuacao += 1
    if tem_numeros:
        pontuacao += 1
    if tem_simbolos:
        pontuacao += 1
    if len(senha) >= 8:
        pontuacao += 1

    faltando = []

    if not tem_minusculas:
        faltando.append("letras minúsculas")
    if not tem_maiusculas:
        faltando.append("letras maiúsculas")
    if not tem_numeros:
        faltando.append("números")
    if not tem_simbolos:
        faltando.append("símbolos")
    if len(senha) < 8:
        faltando.append("mínimo de 8 caracteres")
    if not faltando:
        faltando = "nenhum requisito faltando"
    else:
        faltando = ", ".join(faltando)

    if pontuacao <= 2:
        return f"Senha fraca, pontuacao: {pontuacao}, faltando: {faltando}"
    elif pontuacao <= 4:
        return f"Senha média, pontuacao: {pontuacao}, faltando: {faltando}"
    else:
        return f"Senha forte, pontuacao: {pontuacao}, faltando: {faltando}"
    

def salvar_senha(site, usuario, senha):
    #verifica se o arquivo senhas.json existe, se não existir cria um novo arquivo
    try:
        with open("senhas.json", "r") as arquivo:
            #carrega os dados do arquivo senhas.json
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []
    #adiciona a nova senha ao arquivo senhas.json
    dados.append({"site": site, 
                  "usuario": usuario, 
                  "senha": senha})
    #salva os dados no arquivo senhas.json
    with open("senhas.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def consultar_senhas():
    try:
        with open("senhas.json", "r") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhuma senha salva.")
        return

    if not dados:
        print("Nenhuma senha salva.")
        return

    for numero, senha in enumerate(dados, start=1):
        print(f"--- senha{numero} ---")
        print(f"site: {senha['site']}")
        print(f"usuário: {senha['usuario']}")
        print(f"senha: {senha['senha']}")
        

def excluir_senha():
    try:
        with open("senhas.json", "r") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("nenhuma senha salva.")
        return

    if not dados:
        print("não existem dados no arquivo")
        return

    for numero, senha in enumerate(dados, start=1):
        print(f"--- senha{numero} ---")
        print(f"site: {senha['site']}")
        print(f"usuário: {senha['usuario']}")
        print(f"senha: {senha['senha']}") 

    try:
        numero_excluir = int(input("qual senha quer excluir?: "))
    except ValueError:
        print("digite apenas numeros.")
        return

    if numero_excluir < 1 or numero_excluir > len(dados):
        print("número de senha invalido.")
        return

    dados.pop(numero_excluir - 1)

    with open("senhas.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print("senha excluida com sucesso!")


def editar_senha():
    try:
        with open("senhas.json", "r") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("nenhuma senha salva.")
        return

    if not dados:
        print("não existem dados no arquivo.")
        return

    for numero, senha in enumerate(dados, start=1):
        print(f"--- senha{numero} ---")
        print(f"site: {senha['site']}")
        print(f"usuário: {senha['usuario']}")
        print(f"senha: {senha['senha']}")

    print("digite o número da senha para editar")
    try:
        senha_editar = int(input("nº da senha: "))
    except ValueError:
        print("Digite um valor válido.")
        return

    if senha_editar < 1 or senha_editar > len(dados):
        print("número de senha inválido.")
        return

    senha_selecionada = dados[senha_editar - 1]

    print("-- [1]site [2]usuário [3]senha --")
    pergunta_usuario = input("o que você que alterar? : ")

    if pergunta_usuario == "1":
        site = input("novo site: ")
        senha_selecionada["site"] = site
        print("site alterado com sucesso!")

    elif pergunta_usuario == "2":
        usuario = input("novo usuário: ")
        senha_selecionada["usuario"] = usuario
        print("usuário alterada com sucesso!")

    elif pergunta_usuario == "3":
        senha = input("nova senha: ")
        if len(senha) < 8 or len(senha) > 64:
            print("a senha deve ter entre 8 e 64 caracteres.")
            return

        else:
            senha_selecionada["senha"] = senha
            print("senha alterada com sucesso!")

    with open("senhas.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print("arquivo salvo com sucesso!")


#def buscar_senha()


#def copiar_senha()
        

def menu_interativo():
    while True:
        menu()

        escolha = input("escolha uma opção: ")

        if escolha == "1":
            #gerar senha aleatória
            senha = gerar_senha()
            #verificar força da senha
            forca_senha = verificar_forca_senha(senha)
            #salvar senha no arquivo senhas.json
            site = input("Digite o nome do site: ")
            usuario = input("Digite o nome do usuário: ")
            salvar_senha(site, usuario, senha)
            #exibir a senha gerada e sua força
            print(f"Senha gerada: {senha}")
            print(f"Força da senha: {forca_senha}")
            print("Senha salva com sucesso")

        elif escolha == "2":
            #gerar senha personalizada
            senha_personalizada1 = senha_personalizada()
            #verificar força da senha personalizada
            if senha_personalizada1:
                forca_senha = verificar_forca_senha(senha_personalizada1)
                #salvar senha personalizada no arquivo senhas.json
                site = input("Digite o nome do site: ")
                usuario = input("Digite o nome do usuário: ")
                salvar_senha(site, usuario, senha_personalizada1)
                #exibir a senha personalizada gerada e sua força
                print(f"Senha personalizada gerada: {senha_personalizada1}")
                print(f"Força da senha personalizada: {forca_senha}")
                print("Senha salva com sucesso ")

        elif escolha == "3":
            senha_para_verificar = input("Digite a senha para verificar sua força: ")
            forca_senha = verificar_forca_senha(senha_para_verificar)
            print(f"Força da senha: {forca_senha}")

        elif escolha == "4":
            consultar_senhas()

        elif escolha == "5":
            site = input("digite o site: ")
            usuario = input("digite o usuário/email: ")
            senha = input("digite a senha: ")
            salvar_senha(site, usuario, senha)
            print("senha salva com sucesso")

        elif escolha == "6":
            excluir_senha()

        elif escolha == "7":
            editar_senha()

        elif escolha == "8":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu_interativo()