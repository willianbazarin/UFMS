nota_1 = input('Digite a primeira nota: ')
nota_2 = input('Digite a segunda nota: ')

prim_nota = eval(nota_1)
seg_nota = eval(nota_2)

if nota_1 is nota_2:
    media = (0.4 * prim_nota + 0.6 * seg_nota)
    print(f'sua nota é', {media}, 'esta aprovado')
else:
    media = (0.4 * prim_nota + 0.6 * seg_nota)
    print(f'sua nota é', {media}, 'esta reprovado') 
