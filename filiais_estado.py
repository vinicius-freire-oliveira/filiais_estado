# Lista de estados com possíveis repetições
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

# Armazenando os estados sem repetição de valor usando set e convertendo de volta para lista
estados_unicos = list(set(estados))

# Inicializando uma lista para armazenar listas de valores repetidos de cada estado
lista_de_listas = []
for estado in estados_unicos:
    # Cria uma lista com todas as ocorrências do estado atual
    lista = [uf for uf in estados if uf == estado]
    # Adiciona a lista criada à lista de listas
    lista_de_listas.append(lista)
# Imprime a lista de listas, onde cada sublista contém todos os valores repetidos de um estado
print(lista_de_listas)

# Criando um dicionário onde a chave é o nome de cada estado único e o valor é a contagem de elementos
contagem_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
# Imprime o dicionário com a contagem de ocorrências de cada estado
print(contagem_valores)

# Lista de tuplas, onde cada tupla contém um estado e um número de funcionários
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), 
                ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), 
                ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

# Armazenando os estados sem repetição de valor extraindo apenas os estados das tuplas
estados_unicos = list(set([tupla[0] for tupla in funcionarios]))

# Inicializando uma lista para armazenar listas de valores de funcionários de cada estado
lista_de_listas = []
for estado in estados_unicos:
    # Cria uma lista com todos os números de funcionários para o estado atual
    lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
    # Adiciona a lista criada à lista de listas
    lista_de_listas.append(lista)
# Imprime a lista de listas, onde cada sublista contém os números de funcionários de um estado
print(lista_de_listas)

# Criando um dicionário com dados agrupados de funcionários por estado
agrupamento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
# Imprime o dicionário com os valores de funcionários agrupados por estado
print(agrupamento_por_estado)

# Criando um dicionário com a soma de funcionários por estado
soma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
# Imprime o dicionário com a soma de funcionários por estado
print(soma_por_estado)
