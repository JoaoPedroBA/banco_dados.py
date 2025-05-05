menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação invalida")

    elif opcao == "2":
        valor = float(input("Coloque o valor que deseja retirar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação invalida")

        elif excedeu_limite:
            print("Operação invalida")

        elif excedeu_saques:
            print("Operação invalida")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação invalida")

    elif opcao == "3":
        print("\n-------------- Extrato --------------")
        print("Não foram realizados movimentações bancarias" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------------------")

    elif opcao == "0":
        break
    
    else:
        print("Operação invalida, selecione as opções já criadas.")
