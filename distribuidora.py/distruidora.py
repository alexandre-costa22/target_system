import json

# lê o arquivo JSON com os valores de faturamento diário
with open('dados.json') as json_file:
    faturamento = json.load(json_file)

# lista para armazenar os valores de faturamento diário válidos (ou seja, excluindo os dias sem faturamento)
faturamento_valido = []

# lista para armazenar os dias com faturamento acima da média mensal
dias_acima_media = []

# variáveis para armazenar o menor e maior valor de faturamento
menor_faturamento = float('inf')
maior_faturamento = float('-inf')

# variáveis para calcular a média mensal
soma_faturamento = 0
dias_validos = 0

# percorre os valores de faturamento diário
for dia in faturamento:
    valor = dia['valor']
    if valor > 0:
        
        # se o valor de faturamento é maior que zero, adiciona à lista de faturamento válido e atualiza as variáveis
        faturamento_valido.append(valor)
        soma_faturamento += valor
        dias_validos += 1
        if valor < menor_faturamento:
            menor_faturamento = valor
            
        if valor > maior_faturamento:
            maior_faturamento = valor
            
        if valor > soma_faturamento / dias_validos:
            dias_acima_media.append(dia['dia'])

# calcula a média mensal
media_mensal = soma_faturamento / dias_validos

# imprime os resultados
print('Menor valor de faturamento:', menor_faturamento)
print('Maior valor de faturamento:', maior_faturamento)
print('Número de dias com faturamento acima da média mensal:', len(dias_acima_media))