nota_1 = input('Digite a primeira nota: ')
nota_2 = input('Digite a segunda nota: ')

prim_nota = eval(nota_1)
seg_nota = eval(nota_2)

def media (prim_nota, seg_nota):
    res = (0.4 * prim_nota + 0.6 * seg_nota)
    return res


nota = media(prim_nota, seg_nota)

if nota >= 5:
    print(f'sua nota {nota}', 'APROVADO')

else:
    print(f'sua nota {nota}', 'REPROVADO')

