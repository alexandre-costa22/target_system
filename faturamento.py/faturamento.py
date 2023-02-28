faturamento_por_estado = {
    'São Paulo': 67836.43,
    'Rio de Janeiro': 36678.66,
    'Mato Grosso': 29229.88,
    'Espírito Santo': 27165.48,
    'Outros' : 19846.53
}

valor_total = sum(faturamento_por_estado.values())

for estado, faturamento in faturamento_por_estado.items():
    percentual = (faturamento / valor_total) * 100
    print(f"{estado}: {percentual:.2f}%")