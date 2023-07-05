Mensagem_de_boas_vindas = ("Olá Bem Vindo ao Aplicativo do Banco Dio - Ifood\n Escolha uma das Funcionalidades \n [S] - Sacar \n [D] - Depositar \n [E] - Extrato \n [Q] - Sair do Progama \n ->")
escolha = str(input(Mensagem_de_boas_vindas))

Quantidade_conta = 0
Verific_qtd_saques = 0
Lista_operacoes = ""


escolha = escolha.lower()
while True:

    if escolha == "s":
        if Verific_qtd_saques < 3:
            Valor_saque = float( input("Escolha o valor do saque: ->R$"))
            Verf_valor_conta = Quantidade_conta - Valor_saque
            if Valor_saque > 500:
                print("operação invalida, valor maximo do saque exedido \n")
            elif Verf_valor_conta < 0:
                print("Saldo insuficiente na conta \n")
            else:
                print("Saque feito com sucesso \n")
                Verific_qtd_saques += 1
                Quantidade_conta -= Valor_saque
                informações_saques = f"Saque {Verific_qtd_saques}°, Valor do Saque:R${Valor_saque:.2f}\n"
                Lista_operacoes += informações_saques
        else:
            print("limite de Saques atingido \n")
    
    elif escolha == "d":
        Verf_deposito = float(input("Digite o valor do valor para depositar: ->R$"))
        if Verf_deposito < 0:
            print("Valor invalido para ser depositado \n")
        else:
            print("Valor depositado na conta \n")
            Quantidade_conta += Verf_deposito
            informações_depositos = f"Deposito de R${Verf_deposito:.2f}\n"
            Lista_operacoes+= informações_depositos
    
    elif escolha == "e":
        print("========== Extrato ==========")
        print(Lista_operacoes)
        print("============== ==============")
        print(f"Valor na conta:R${Quantidade_conta:.2f}")

    elif escolha =="q":
        print("finalizado o Progama \n")

        break
    else:
        print("Escolha uma operação valida \n")

    escolha = input(Mensagem_de_boas_vindas)
    escolha = escolha.lower()


print("Obrigado por usar o Banco Dio - Ifood")
