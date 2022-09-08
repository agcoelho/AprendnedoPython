class Pessoa:
    def __init__(self, nome, cpf, cargo):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo


class Vendedor(Pessoa):

    def cal_salario(self):
        salario = 1500.00
        vendas = float(input('digite quanto você vendeu\n'))
        salario = salario + (vendas * 0.30)
        print(f'{self.nome}, {self.cpf}, {self.cargo}, seu salario é de {salario}')


class Caixa(Pessoa):
    def cal_salario(self):
        ht = float(input(('digite suas horas trabalhadas\n')))
        dado = float(input('digite quanto ganha por hora\n'))
        salario = dado * ht
        print(f'{self.nome}, {self.cpf}, {self.cargo}, seu salário é de: {salario}')


class Gerente(Caixa):
    pass




