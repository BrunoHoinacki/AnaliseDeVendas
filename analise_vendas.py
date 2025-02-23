import csv

# Dicionários para armazenar os dados
totais_vendas = {}
produtos_vendidos = {}
estoque_sugerido = {}

# Ler o arquivo CSV
with open('vendas_dez_fev.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        empreendedor = linha['empreendedor']
        produto = linha['produto']
        quantidade = int(linha['quantidade'])
        valor = float(linha['valor_unitario'])

        # Calcular total de vendas
        total_venda = quantidade * valor
        if empreendedor in totais_vendas:
            totais_vendas[empreendedor] += total_venda
        else:
            totais_vendas[empreendedor] = total_venda

        # Registrar produtos vendidos
        if empreendedor not in produtos_vendidos:
            produtos_vendidos[empreendedor] = {}
        if produto in produtos_vendidos[empreendedor]:
            produtos_vendidos[empreendedor][produto] += quantidade
        else:
            produtos_vendidos[empreendedor][produto] = quantidade

# Identificar o mais vendido e sugerir estoque
for empreendedor in produtos_vendidos:
    mais_vendido = max(produtos_vendidos[empreendedor], key=produtos_vendidos[empreendedor].get)
    qtd_mais_vendido = produtos_vendidos[empreendedor][mais_vendido]
    estoque_sugerido[empreendedor] = f"{mais_vendido}: {qtd_mais_vendido + 10} unidades"

# Exibir relatórios
print("Relatório de Vendas (Dezembro 2024 a Fevereiro 2025):")
print("\nTotais de Vendas:")
for empr, total in totais_vendas.items():
    print(f"{empr}: R$ {total:.2f}")

print("\nProduto Mais Vendido por Empreendedor:")
for empr in produtos_vendidos:
    mais_vendido = max(produtos_vendidos[empr], key=produtos_vendidos[empr].get)
    print(f"{empr}: {mais_vendido} ({produtos_vendidos[empr][mais_vendido]} unidades)")

print("\nSugestão de Estoque:")
for empr, sugestao in estoque_sugerido.items():
    print(f"{empr}: {sugestao}")