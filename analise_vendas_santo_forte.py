import pandas as pd
import glob

# Lista dos arquivos CSV de diferentes meses
file_paths = [
    'C:/Users/BrunoSantanadeSa/Documents/pessoal/analise/santo_forte_sales_combined_filtrado.csv',
    # Adicione aqui os caminhos dos outros arquivos CSV
]

def load_csv(file_path, encoding):
    try:
        return pd.read_csv(file_path, encoding=encoding)
    except UnicodeDecodeError:
        print(f"Erro de codificação ao ler {file_path} com a codificação {encoding}.")
        return None

# Tentar com várias codificações
encodings = ['utf-8', 'ISO-8859-1', 'latin1']
df_list = []

for file_path in file_paths:
    for encoding in encodings:
        df = load_csv(file_path, encoding)
        if df is not None:
            df_list.append(df)
            break

if df_list:
    df = pd.concat(df_list, ignore_index=True)

    # Renomear as colunas para remover possíveis espaços e garantir consistência
    df.columns = df.columns.str.strip()

    # Adicionando coluna de receita
    df['Receita'] = df['Quantity'] * df['Total Price']

    # Converter a coluna 'Date' para o formato datetime sem especificar o formato
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Coerce irá transformar erros em NaT

    # Verificar se há algum erro na conversão e lidar com eles
    if df['Date'].isna().sum() > 0:
        print("Aviso: Alguns valores de data não puderam ser convertidos.")

    # Adicionando coluna de Mês
    df['Mês'] = df['Date'].dt.to_period('M')

    # Total de Vendas
    total_vendas = df['Receita'].sum()
    print(f'Total de Vendas: R${total_vendas:.2f}')

    # Itens Mais Vendidos
    itens_mais_vendidos = df.groupby('Product Name')['Quantity'].sum().sort_values(ascending=False)
    print('Itens Mais Vendidos:')
    print(itens_mais_vendidos)

    # Receita por Item
    receita_por_item = df.groupby('Product Name')['Receita'].sum().sort_values(ascending=False)
    print('Receita por Item:')
    print(receita_por_item)

    # Vendas por Período (Exemplo: por mês)
    vendas_por_mes = df.groupby('Mês')['Receita'].sum()
    print('Vendas por Mês:')
    print(vendas_por_mes)

    # Vendas por Cidade
    vendas_por_cidade = df.groupby('City')['Receita'].sum().sort_values(ascending=False)
    print('Vendas por Cidade:')
    print(vendas_por_cidade)
else:
    print("Nenhum arquivo CSV pôde ser carregado.")

