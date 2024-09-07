import pandas as pd
import matplotlib.pyplot as plt

# Exemplo de dados baseados na sua saída
total_vendas = 67410.00

itens_mais_vendidos = pd.Series({
    'Camiseta Santo Forte KKK': 121.0,
    'Camiseta Santo Forte Gato Felix Baby Look': 82.0,
    'Camiseta Santo Forte Gato Felix': 79.0,
    'Caneca Santo Forte Gato Felix Coffee Time': 76.0,
    'Caneca Santo Forte Tigres': 71.0,
    'Camiseta Santo Forte Mulher com Coração Farpado': 46.0,
    'Caneca Santo Forte Portal Mágico': 32.0
})

receita_por_item = pd.Series({
    'Camiseta Santo Forte KKK': 17460.0,
    'Camiseta Santo Forte Gato Felix Baby Look': 11880.0,
    'Camiseta Santo Forte Gato Felix': 10980.0,
    'Caneca Santo Forte Gato Felix Coffee Time': 9400.0,
    'Caneca Santo Forte Tigres': 7650.0,
    'Camiseta Santo Forte Mulher com Coração Farpado': 6240.0,
    'Caneca Santo Forte Portal Mágico': 3800.0
})

vendas_por_mes = pd.Series({
    '2024-01': 4040.0,
    '2024-02': 7490.0,
    '2024-03': 8120.0,
    '2024-04': 6840.0,
    '2024-05': 7440.0,
    '2024-06': 10690.0,
    '2024-07': 15580.0,
    '2024-08': 7210.0
})

vendas_por_cidade = pd.Series({
    'São Paulo': 17240.0,
    'Guarulhos': 12990.0,
    'São Bernardo': 9940.0,
    'São Caetano': 9430.0,
    'Santo André': 9160.0,
    'Arujá': 8410.0
})

# Gráfico do Total de Vendas como Pie Chart (Gráfico de Pizza)
plt.figure(figsize=(10, 6))
# Apenas para exemplo, aqui estamos criando uma única fatia
# Para um gráfico mais informativo, você precisaria de múltiplos dados ou categorias
plt.pie([total_vendas], labels=['Total de Vendas'], autopct='%1.1f%%', colors=['blue'])
plt.title('Total de Vendas (Gráfico de Pizza)')
plt.show()

# Gráfico do Total de Vendas como Gráfico de Linha (se aplicável)
# Este gráfico é mais útil se você tiver dados históricos ou categorias comparativas
plt.figure(figsize=(10, 6))
# Aqui estamos apenas criando um gráfico de linha com uma única série de dados
# Isso mostra o valor total com um ponto
plt.plot(['Total de Vendas'], [total_vendas], marker='o', color='blue')
plt.title('Total de Vendas (Gráfico de Linha)')
plt.ylabel('Valor (R$)')
plt.xticks(['Total de Vendas'])
plt.grid(True)
plt.show()

# Gráfico dos Itens Mais Vendidos
plt.figure(figsize=(12, 8))
itens_mais_vendidos.plot(kind='bar', color='green')
plt.title('Itens Mais Vendidos')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico da Receita por Item
plt.figure(figsize=(12, 8))
receita_por_item.plot(kind='bar', color='purple')
plt.title('Receita por Item')
plt.xlabel('Produto')
plt.ylabel('Receita (R$)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gráfico das Vendas por Mês
plt.figure(figsize=(12, 8))
vendas_por_mes.plot(kind='line', marker='o', color='red')
plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Receita (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico das Vendas por Cidade
plt.figure(figsize=(12, 8))
vendas_por_cidade.plot(kind='bar', color='orange')
plt.title('Vendas por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Receita (R$)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
