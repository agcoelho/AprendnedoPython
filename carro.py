import random

velo = random.randint(50, 100)

if velo > 80:
    multa = (velo - 80) * 7
    print('vc ultrapassou a velocidade com {}Km/h sua multa é de {} reais'.format(velo, multa))

else:
    print('parabens vc está a {}Km/h :)'.format(velo))
