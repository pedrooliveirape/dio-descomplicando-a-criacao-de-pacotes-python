from .transformartxt import arquivoexiste, lerarquivo

def precoporlitro(nome):
    try:
        arquivoexiste(nome)
    except:
        print('Erro. Arquivo não encontrado!')
    else:
        try:
            lista = lerarquivo(nome)
            for nalista in lista:
                ppl = f'{nalista[2] / nalista[1]:.2f}'
                nalista.append(float(ppl))
                del nalista[2]
                del nalista[1]
        except:
            print('Erro ao calcular preço por litro!')
        else:
            return lista


def melhorpreco(nome):
    lista_produtos = precoporlitro(nome)
    melhor_preco = []
    for contagem, valores in enumerate(lista_produtos):
        if contagem == 0:
            melhor_preco.append(valores[0])
            melhor_preco.append(valores[1])
        else:
            if melhor_preco[1] > valores[1]:
                melhor_preco.clear()
                melhor_preco.append(valores[0])
                melhor_preco.append(valores[1])
    return melhor_preco