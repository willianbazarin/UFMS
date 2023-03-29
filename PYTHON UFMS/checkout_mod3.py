tempo_de_viagem = input ('Informe o tempo de viagem em minutos: ')
distancia_percorrida = input('Informe a distancia percorrida em km: ')
consumo_combustivel_por_km = input('Informe o consumo medio de km por litro: ')

t_viagem = (int(tempo_de_viagem) / 60)
distancia_int = int (distancia_percorrida)
consumo_int = int (consumo_combustivel_por_km)

print (f'tempo de viagem é: {t_viagem}Hs')
print (f'consumo medio: {distancia_int / consumo_int}')





