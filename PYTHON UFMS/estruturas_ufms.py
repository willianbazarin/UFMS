altura = input('digite sua altura: ')
sexo = input('digite (h)omens e (m)ulheres: ')

alt = eval(altura)



if sexo == 'h':
    peso = (72.7 * alt) - 58
    print (peso)
elif sexo == 'm':
    peso = (62.1 * alt) - 44.7
    print (peso)


