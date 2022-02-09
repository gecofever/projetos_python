ARQ = "c:\\banco.txt"
FIM = 0
contas = []

def le_arquivo():
    with (open(ARQ, "r")) as arquivo:
        linha = arquivo.readline()
        while (linha != ""):
            linha = linha.strip("\n")
            linha = linha.split(";")
            nconta = int(linha[0])
            nome = (linha[1])
            saldo = float(linha[2])
            cliente = [nconta, nome, saldo]
            contas.append(cliente)
            linha = arquivo.readline()

def grava_arquivo(contas):
    with open(ARQ, "w") as clientes:
        for cliente in contas:
            clientes.write(str(cliente[0]) + ";" + str(cliente[1]) + ";" + str(cliente[2]) + "\n")
    print ("ARQUIVO GRAVADO")

def saldo_geral():
    for i in range (len(contas)):
        print (contas[i])

def inteiro_menu():
    opcao_ok = False
    while (not opcao_ok):
        try:
            opcao = int(input("Escolha uma opção: "))
        except:
            print("Erro: entrada inválida")
        else:
            return int(opcao)

def entra_inteiro():
    opcao_ok = False
    while (not opcao_ok):
        try:
            conta = int(input("Digite numero de conta: "))
        except:
            print("Erro: entrada inválida")
        else:
            return int(conta)

def entra_float():
    opcao_ok = False
    while (not opcao_ok):
        try:
            saldo = float(input("Digite valor do saldo: "))
        except:
            print("Erro: entrada inválida")
        else:
            return float(saldo)

def saldo_vip():
    contas_vip = []
    saldo = entra_float ()
    for i in range (len(contas)):
        if (contas [i][2] > saldo):
            contas_vip.append(contas[i])
    print (contas_vip)
    return opcao

def saldo_negativo():
    contas_negativas = []
    for i in range (len(contas)):
        if (contas [i][2] < 0):
            contas_negativas.append(contas[i])
    print(contas_negativas)

def indice_conta():
    nconta = entra_inteiro()
    for i in range (len(contas)):
        if nconta == contas [i][0]:
            return i
    return None

def verifica_saldo():
    saldo = entra_float()
    if saldo >= 0:
        return saldo
    return True

def verifica_nome():
    nome = input("Inserir Nome Completo do cliente: ")
    nomes_separados = nome.split(' ')
    for letra in nome:
        if letra.isdigit():
            print("Sem Números")
            return True
    if len(nomes_separados) < 2:
        print("Digite Nome e Sobrenome")
        return True
    return nome

def verifica_conta():
    nconta = entra_inteiro()
    for i in range (len(contas)):
        if nconta == contas[i][0]:
            print ("Conta já existe, Não é posível criar essa conta!")
            return True
    return nconta

def insere_conta():
    nconta = verifica_conta()
    if nconta != True:
        nome = verifica_nome()
        if nome != True:
            saldo = verifica_saldo()
            if saldo != True:
                nova_conta = [nconta, nome, saldo]
                contas.append(nova_conta)
                print(contas)

def altera_saldo():
    opcao_ok = False
    i = indice_conta()
    if i != None:
        while (not opcao_ok):
            try:
                operacao = input("Você deseja realizar Saque ou Depósito (S/D)?: ")
                if operacao in "Dd":
                    deposito = float(input("Informe valor do Depósito: "))
                    contas[i][2] = contas[i][2] + deposito
                    opcao_ok = True
                elif operacao in "Ss":
                    saque = float(input("Informe valor do Saque: "))
                    contas[i][2] = contas[i][2] - saque
                    opcao_ok = True
            except ValueError:
                print("Erro: entrada inválida")
    else:
        print("Conta Não Existe!!!")
    print (contas)

def exclui_conta():
    i = indice_conta()
    if i != None:
        if contas [i][2] == 0:
            contas.pop(i)
            print (contas)
        else:
            print ("ESSA CONTA NÃO PODE SER EXCLUÍDA")
    else:
        print("Conta Não Existe!!!")
        print (contas)

def entra_opcao():
    opcao = inteiro_menu()
    if (opcao < 0) or (opcao > 4):
        print("Erro: opção inválida")
    return opcao

def escolha_gerencia():
    opcao = inteiro_menu()
    if (opcao < 0) or (opcao > 3):
        print("Erro: opção inválida")
    return opcao

def menu_principal():
    while True:
        print("Menu")
        print("[1] - Inclusao de Conta")
        print("[2] - Alteração de Saldo")
        print("[3] - Exclusão de Conta")
        print("[4] - Relatório Gerencial")
        print("[0] - Sair")
        return entra_opcao()

def menu_gerencia():
    while True:
        print("Menu Gerência")
        print("[1] - Listar Clientes Negativados")
        print("[2] - Listar Clientes VIP")
        print("[3] - Listar todas as Contas")
        print("[0] - Voltar")
        return escolha_gerencia()

def menus():
    if (opcao == 1):
        insere_conta()
    elif (opcao == 2):
        altera_saldo()
    elif (opcao == 3):
        exclui_conta()
    elif (opcao == 4):
        gerente = menu_gerencia()
        while (gerente != FIM):
            if (gerente == 1):
                saldo_negativo()
            elif (gerente == 2):
                saldo_vip()
            elif (gerente == 3):
                saldo_geral()
            gerente = menu_gerencia()

le_arquivo()
print (contas)
opcao = menu_principal()
while (opcao != FIM):
    menus()
    opcao = menu_principal()
print("Fim do programa")
grava_arquivo(contas)