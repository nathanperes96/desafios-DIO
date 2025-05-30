menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou, o valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        excedeu = valor > saldo

        excedeu_limite = valor > limite

        limite_saque = numero_saques >= LIMITE_SAQUES

        if excedeu:
            print("Não tem saldo suficiente. ")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif limite_saque:
            print("Limite de saque atingido, Volte amanhã. ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}"
            numero_saques += 1

        else:
            print("Valor inválido")
    
    elif opcao == "e":
        print(f"Saldo atual: R${saldo:.2f}")
        print("Extrato")

    elif opcao == "q":
        print("Saindo do sistema...")
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
