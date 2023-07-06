
def menu():
    Mensagem_de_boas_vindas = ("Olá Bem Vindo ao Aplicativo do Banco Dio - Ifood\n Escolha uma das Funcionalidades \n [S] - Sacar \n [D] - Depositar \n [E] - Extrato \n [NC] - Nova conta \n [LC] - Listar contas \n [NU] - Novo Usuário \n [Q] - Sair do Progama \n ->")
    escolha = str(input(Mensagem_de_boas_vindas))
    escolha = escolha.lower()
    return escolha


def saque(*,saldo,valor,extrato,limite, numero_saque,limite_saques):

    Verf_valor_conta = saldo - valor
    Verific_qtd_saques = numero_saque < limite_saques
    if Verific_qtd_saques:
        if valor > limite:
            print("operação invalida, valor maximo do saque exedido \n")
        elif Verf_valor_conta < 0:
            print("Saldo insuficiente na conta \n")
        else:
            print("Saque feito com sucesso \n")
            Verific_qtd_saques += 1
            saldo -= valor
            informações_saques = f"Saque {Verific_qtd_saques}°, Valor do Saque:R${valor:.2f}\n"
            extrato += informações_saques
           
    else:
        print("Valor maximo de saques exedido")
        
    return saldo, extrato

def deposito(*,saldo,valor,extrato):
    if valor < 0:
        print("Valor invalido para ser depositado \n")
    else:
        print("Valor depositado na conta \n")
        saldo += valor
        informações_depositos = f"Deposito de R${valor:.2f}\n"
        extrato += informações_depositos

    return saldo,extrato

def exibir_extrato(saldo,extrato):
    print("========== Extrato ==========")
    print(extrato)
    print("============== ==============")
    print(f"Valor na conta:R${saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número):")
    usuarios = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("Usuario ja cadastrado com esse CPF!!")
        return
    nome = input("Informe o nome completo: ->")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (lagradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "Data_nascimento": data_nascimento, "Cpf": cpf, "Endereço": endereco})
    print("Usuario criado com sucesso")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuarios for usuarios in usuarios if usuarios["cpf"]== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"Agencia": agencia, "Numero_conta": numero_conta, "Usuario": usuario}
def listar_contas(contas):
    for conta in contas:
        print(f"Agencia:{conta['agencia']}")
        print(f"C/C: {conta['numero_conta']}")
        print(f"Titular:{conta['usuario']['nome']}\n")


def main():
    Quantidade_conta = 0
    limite_saque = 3
    Verific_qtd_saques = 0
    limite = 500
    Lista_operacoes = ""
    escolha = menu()
    lista_usuarios = []
    agencia = "0001"
    contas = []

    while True:

        if escolha == "s":
            Valor_saque = float( input("Escolha o valor do saque: ->R$"))
            Quantidade_conta, Lista_operacoes = saque(saldo = Quantidade_conta,
                  valor = Valor_saque,
                  extrato =Lista_operacoes,
                  limite= limite,
                  numero_saque=Verific_qtd_saques,
                  limite_saques=limite_saque)
            
        elif escolha == "d":
            Valor_deposito = float(input("Digite o valor do valor para depositar: ->R$"))
            Quantidade_conta, Lista_operacoes = deposito(saldo = Quantidade_conta,
                valor = Valor_deposito,
                extrato = Lista_operacoes)
        
        elif escolha == "e":
            exibir_extrato()

        elif escolha =="q":
            print("finalizado o Progama \n")

            break
        
        elif escolha == "nc":
            numero_conta = len(contas)+1
            contas = criar_conta(agencia,numero_conta,lista_usuarios)

            if contas:
                contas.append(contas)

        elif escolha == "lc":
            listar_contas(contas)

        elif escolha == "nu":
            criar_usuario(lista_usuarios)
        
        else:
            print("Escolha uma operação valida \n")

        escolha = input(menu)


    print("Obrigado por usar o Banco Dio - Ifood")

main()