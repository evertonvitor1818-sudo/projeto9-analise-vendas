import pandas as pd

def limpar_dados(df):
    # Remover colunas desnecessárias
    colunas_para_remover = ['coluna1', 'coluna2']  # Substitua pelos nomes das colunas a serem removidas
    df = df.drop(columns=colunas_para_remover)

    # Tratar valores ausentes
    df = df.fillna(method='ffill')  # Preencher valores ausentes com o valor anterior

    # Converter tipos de dados, se necessário
    df['coluna3'] = df['coluna3'].astype(int)  # Substitua 'coluna3' pelo nome da coluna a ser convertida

    return df
