menu = """
Olá, o que podemos fazer por você?

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair


"""

saldo = 0 
extrato = ''
n_saque = 0
n_diario = 0
LIMIT_SAQUE = 3
LIMIT_DIARIO = 500

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Quanto você deseja depositar?: "))
        if(deposito> 0):
            saldo += deposito
            extrato += f"R$  {deposito}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para o depósito. Por favor, escolha um valor válido.")

    elif opcao == '2':
        saque = float(input("Quanto voce deseja sacar?: "))
        if(n_saque<LIMIT_SAQUE):
            if(n_diario <LIMIT_DIARIO):
                if(n_diario + saque <= LIMIT_DIARIO):
                    if(saldo>=saque):
                        saldo -= saque
                        n_diario += saque
                        n_saque += 1
                        extrato += f"R$ -{saque}\n"
                        print("Seu saque está disponível")
                    else:
                        print("Saque maior que o saldo da conta")
                else:
                    print(f"O seu saque está ultrapassando o seu limite diário. Você pode sacar até {LIMIT_DIARIO-n_diario} R$ hoje.")
            else:
                print("Você ultrapassou seu limite diário. Por favor, volte amanhã.")
        else: 
            print("Voce já realizou três saques hoje. Por favor, volte amanhã.")

    elif opcao == '3':
        if(extrato is ''):
            print('Sua conta está zerada. Por favor, realize um depósito.')
        else:
            print(extrato,end='\n')
            print(f'Seu saldo atual é {saldo} R$.')
    
    elif opcao == '4':
        break
    else:
        print("Operação inválida, por favor selecione uma opção válida")

else: 
    print("Obrigado por ser nosso cliente!")
                               
