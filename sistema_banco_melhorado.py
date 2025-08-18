def menu():
    menu = """
Bem-vindo ao KiBank! Onde seu dinheiro rende e você gerencia de forma simples.
=========== MENU ===========
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=> """
    return input(menu).strip().lower()

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso!")
    else:
        print("❌ Valor inválido para depósito.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("❌ Falha! Saldo insuficiente.")
    elif excedeu_limite:
        print("❌ Falha! Limite de saque excedido.")
    elif excedeu_saques:
        print("❌ Falha! Limite de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso.")
    else:
        print("❌ Falha! Valor inválido para saque.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, *, extrato):
    print("\n=========== EXTRATO ===========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("================================")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário (somente números): ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("❌ Já existe um usuário com esse CPF.")
        return
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("✅ Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("✅ Conta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero,
            "usuario": usuario
        }
    print("❌ Usuário não encontrado. Crie o usuário primeiro com a opção [nu].")
    return None

def listar_contas(contas):
    if not contas:
        print("⚠️ Nenhuma conta cadastrada.")
        return
    print("\n=========== LISTA DE CONTAS ===========")
    for conta in contas:
        linha = f"""
Agência: {conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
"""
        print("=" * 40)
        print(linha)
    print("========================================")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("👋 Obrigado por usar o KiBank. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

main()
