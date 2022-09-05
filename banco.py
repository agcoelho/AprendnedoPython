import sys

validacao = 0
while validacao != 's' and validacao != 'S':
    name = input('digite seu nome\n')
    fpc = int(input('digite seu cpf\n'))
    numero = int(input('digite sua conta\n'))

    dados = {'nome': name, 'cpf': fpc, 'conta': numero}
    print(f'seus dados estão corretos? {dados}')
    validacao = input('digite "s" para "sim" e "n" para "nao"\n')


senha = ''
while senha != '123456':
    senha = input('digite sua senha\n')
    if senha != '123456':
        print('senha incorreta, tente novamente\n')

print('bem-vindo ao banco')
saldo = 100.00
escolha1 = ''
while True:
    escolha = int(input('o que deseja fazer?\nSacar - 1\nDepositar - 2\nTransferir - 3\nVer Saldo - 4\nSair - 5\n'))

    if escolha == 1:
        saque = 0
        while saldo < saque or saque <= 0:
            saque = float(input('quanto deseja sacar?'))
            if saldo < saque or saque <= 0:
                print('valor invalido ou saldo insuficiente')
            opcao = input('deseja continuar? (s/n)')
            if opcao == 'n' or opcao == 'N':
                sys.exit()
            saldo = saldo - saque
        print(f'saque no valor de R${saque} realizado com sucesso, seu saldo atual é de {saldo}')
    elif escolha == 2:
        deposito = 0
        while deposito <= 0:
            deposito = float(input('digite o valor que deseja depositar\n'))
            if deposito <= 0:
                opcao2 = input('valor do deposito invalido, deseja tentar novamente? (s/n)')
                if opcao2 == 'n' or opcao2 == 'N':
                    sys.exit()
        saldo = saldo + deposito
        print(f'deposito no valor de R${deposito} feito com sucesso, seu saldo agora é de R${saldo}')
    elif escolha == 3:
        transferencia = 0
        while transferencia > saldo or transferencia <= 0:
            transferencia = float(input('digite quanto deseja transferir\n'))
            if transferencia > saldo or transferencia <= 0:
                opcao3 = input('valor invalido deseja tentar novamente? (s/n)\n')
                if opcao3 == 'n' or opcao3 == 'N':
                    sys.exit()
        pessoa = input('digite para quem deseja transferir\n')
        saldo = saldo - transferencia
        print(f'trasnferencia de {transferencia} realizada com sucesso para {pessoa}, seu saldo agora é de {saldo}\n')

    elif escolha == 4:
        print(f'seu saldo é de R${saldo}')

    elif escolha == 5:
        sys.exit()
    elif escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
        print('opção inválida')





