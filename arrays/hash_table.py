len_tabela = 10
tabela = [[] for i in range(len_tabela)]

def hash_function(tamanho_tabela, chave):
    return len(chave) % tamanho_tabela


def inserir(tabela, chave, valor):
    indice = hash_function(len(tabela), chave)

    tabela[indice] = (chave, valor)

    
inserir(tabela, "nome", "Ycaro")
print(tabela)