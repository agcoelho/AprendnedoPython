n1 = float(input('digite a primeira nota\n'))
n2 = float(input('digite a segunda nota\n'))
n3 = float(input('digite a terceira nota\n'))
n4 = float(input('digite a quarta nota\n'))
total = (n1 + n2 + n3 + n4)/4

if total >= 5:
    print('aluno aprovado com a media: {}'.format(total))


else:
    print('aluno reprovado com a media: {}'.format(total))
