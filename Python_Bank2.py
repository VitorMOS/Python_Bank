
import textwrap

def menu():
    menu = """
Olá, o que podemos fazer por você?
/n
=========== MENU =================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar usuário
[5] Criar conta
[6] Sair

=================================
""" 
    return input(textwrap.dedent(menu))

def verificar(contas):
    conta = input("Qual o número da conta?: ")
    chaves = contas.keys();
    if (conta in chaves):
        val1 = 1
        saldo = contas[conta]["saldo"] 
        extrato = contas[conta]["extrato"]
        senha = contas[conta]["senha"]
        n_diario = contas[conta]["n_diario"]
        n_saque = contas[conta]["n_saque"]
    else:
        val1 = 0
        saldo = 0
        extrato = "conta não existente"
        senha = 0
        n_diario = 0
        n_saque = 0
    return (conta, val1, extrato, saldo, senha, n_diario, n_saque)
 
def depositar(extrato, saldo):
    deposito = float(input("Quanto você deseja depositar?: "))
    if(deposito> 0):
        saldo += deposito
        extrato += f"R$  {deposito}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido para o depósito. Por favor, escolha um valor válido.")
    return (extrato, saldo)

def senhar(senha):
    tentativa = input("Qual a senha da conta?: ")
    if(tentativa == senha):
        val2 = 1
    else:
        print("Senha inválida. Por favor, tente novamente.")
        val2 = 0
    return val2

def sacar(saldo, n_diario, n_saque, extrato):
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
    
    return (saldo, n_diario, n_saque, extrato)

def exibir(extrato, saldo):
    if(extrato is ''):
        print('Sua conta está zerada. Por favor, realize um depósito.')
    else:
        print(extrato,end='\n')
        print(f'Seu saldo atual é {saldo} R$.')

def cadastro(usuarios):
    sugestao = input("Por favor, informe o seu cpf: ")
    cpf = usuarios.keys()
    if(sugestao in cpf):
        print("Usuario com cpf já cadastrado.")
    else:
        nome = input("Qual o seu nome? ")
        cep = input("Qual o seu CEP? ")
        usuarios.update({sugestao:{"nome": nome, "cep": cep}})
    return  usuarios

def cpf(cpf1, usuarios): 
    chaves = usuarios.keys()
    if(cpf1 in chaves):
        val3 = 1
    else:
        val3 = 0
    return val3


def conta(contas):
    lista_contas = contas.keys()
    quant_contas = len(lista_contas)
    numero_nova = str(quant_contas+1).zfill(5)
    senha = input("Qual a senha desejada para sua conta?")
    contas.update({numero_nova:{"saldo": 0, "extrato": '', "senha":senha, "n_diario": 0,"n_saque": 0}})
    print(f"Sua conta foi criada com o numero {numero_nova}")

    return contas
        
def atualizar(contas, conta, extrato, saldo, n_diario, n_saque, senha):
    contas.update({conta:{"extrato":extrato, "n_saque":n_saque, "n_diario":n_diario, "saldo":saldo, "senha":senha}})

    return contas


LIMIT_SAQUE = 3
LIMIT_DIARIO = 500
contas = {}
usuarios = {}

while True:

    opcao = menu()

    if opcao == "1":
        (conta, val1, extrato, saldo, senha, n_diario, n_saque) = verificar(contas)
        if(val1 == 1):
            (extrato, saldo) = depositar(extrato, saldo)
            contas = atualizar(contas, conta, extrato, saldo, n_diario, n_saque, senha)
        else:
            print("Conta digitada é inválida. Por favor, tente novamente.")

    elif opcao == '2':
        (conta, val1, extrato, saldo, senha, n_diario, n_saque) = verificar(contas)
        if(val1 == 1):
            val2 = senhar(senha)
            if(val2 == 1):
                 (saldo, n_diario, n_saque, extrato) = sacar(saldo, n_diario, n_saque, extrato)
                 contas = atualizar(contas, conta, extrato, saldo, n_diario, n_saque, senha)
            else:
                print("A senha digitada está inválida. Por favor, tente novamente.")
        else:
            print("Conta digitada é inválida. Por favor, tente novamente.")
    elif opcao == '3':
        (conta, val1, extrato, saldo, senha, n_diario, n_saque) = verificar(contas)
        if(val1 == 1):
            val2 = senhar(senha)
            if(val2 == 1):
                exibir(extrato, saldo)
            else:
                print("A senha digitada está inválida. Por favor, tente novamente.")
        else:
            print("Conta digitada é inválida. Por favor, tente novamente.")
    elif opcao == '4':
        usuarios = cadastro(usuarios)
    elif opcao == '5':
        cpf1 = input("Por favor, informe o seu cpf: ")
        val3 = cpf(cpf1, usuarios)
        if(val3 == 1):
            contas = conta(contas)
        else:
            print("Usuário não cadastrado")
    elif opcao == '6':
        break
    else:
        print("Operação inválida, por favor selecione uma opção válida")

else: 
    print("Obrigado por ser nosso cliente!")
                               
