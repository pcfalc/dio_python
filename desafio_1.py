menu = f'''
--------------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
--------------
'''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        #print("Deposito")
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print("Valor invalido")

    elif opcao == 's':
        #print("Saque")
        valor = float(input("Informe o valor do saque: "))

        execedeu_saldo = valor > saldo
        execeu_limite = valor > limite
        execeu_saque = numero_saque >= LIMITE_SAQUE

        if execedeu_saldo:
            print("Voce não possui saldo suficiente")

        elif execeu_limite:
            print("Numero maximo de saque excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1

        else:
            print("Valor informado invalido")

    elif opcao == 'e':
        #print("Extrato")
        print("\n======== EXTRATO ========")
        print("Nao foram realizados movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n======== FIM ========")
    
    elif opcao == 'q':
        print("Sair")
        break

    else:
        print("Opção invalida")
