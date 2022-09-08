from calc_salario.vendas import Caixa
from calc_salario.vendas import Vendedor
from calc_salario.vendas import Gerente

opcao = 'n'
cargo = ' '
while opcao != 's':
    cargo = input('digite seu cargo\n')
    if cargo == 'vendedor' or cargo == 'Vendedor' or cargo == 'caixa' or cargo == 'Caixa' or cargo == 'gerente' or cargo == 'Gerente':
            print(f'o cargo escolhido foi {cargo}')
            opcao = input('seu cargo está correto? (s/n)')
    else: print('cargo invalido')


if cargo == 'vendedor' or cargo == 'Vendedor':
    nome = input('digite seu nome\n')
    cpf = input('digite seu cpf\n')
    if cpf == '123':
        senha = '0'
        while senha != '123':
            senha = input('digite sua senha\n')
            if senha != '123':
                print('senha incorreta tente novamente\n')

    p1 = Vendedor(nome, cpf, cargo)
    p1.cal_salario()

elif cargo == 'caixa' or cargo == 'Caixa':
    nome = input('digite seu nome\n')
    cpf = input('digite seu cpf\n')
    if cpf == '321':
        senha = '0'
        while senha != '321':
            senha = input('digite sua senha\n')
            if senha != '321':
                print('senha incorreta tente novamente\n')

    p2 = Caixa(nome, cpf, cargo)
    p2.cal_salario()

elif cargo == 'gerente' or cargo == 'Gerente':
    nome = input('digite seu nome\n')
    cpf = input('digite seu cpf\n')
    if cpf == '041':
        senha = '0'
        while senha != '041':
            senha = input('digite sua senha\n')
            if senha != '041':
                print('senha incorreta tente novamente\n')

    p3 = Gerente(nome, cpf, cargo)
    p3.cal_salario()




