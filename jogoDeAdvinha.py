import random

player = int(input('digite um numero de um a cinco\n'))
n = random.randint(0,5)

if player == n:
    print('vc acertou, o numero é {}'.format(n))

else:
    print(('vc errou, o numero era {}'.format(n)))



