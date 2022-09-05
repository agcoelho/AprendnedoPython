frase = input('digite seu nome\n')

print(frase.upper())
print(frase.lower())
espacos = frase.count(' ') #contando letras sem espaços
total = (len(frase)) - espacos
print(total)
print(len(frase[:frase.find(' ')])) #contando primeiro nome

