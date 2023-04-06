def ler_produtos():
    n = int(input())
    produtos = {}
    for i in range(n):
        nome = input()
        preco = float(input())
        if nome in produtos:
            print("Produto já cadastrado")
        else:
            produtos[nome] = preco
    return produtos

def buscar_preco(produtos):
    while True:
        nome = input()
        if nome == "Fim":
            break
        elif nome in produtos:
            print(produtos[nome])
        else:
            print("Produto nao cadastrado")

produtos = ler_produtos()
buscar_preco(produtos)
