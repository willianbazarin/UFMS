def calcular_consumo(velocidade_media, tempo, autonomia):
    distancia=velocidade_media * tempo
    consumo = distancia / autonomia
    return consumo


velocidade_media = float(input())
tempo = float(input())
autonomia = float(input())
consumo = calcular_consumo(velocidade_media, tempo, autonomia)
print (consumo)
