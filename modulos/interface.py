import pandas as pd
import matplotlib.pyplot as plt

def sistema_etl_terminal():
    print("--- FASE 1: INGESTÃO (Digite os dados e aperte Enter) ---")
    print("Formato: DATA,PRODUTO,VALOR,ESTADO")
    print("Digite 'FIM' para encerrar e gerar o gráfico.\n")

    linhas_brutas = []
    
    while True:
        entrada = input("Próxima linha: ")
        
        if entrada.upper() == 'FIM':
            break
        
        if entrada.strip() == "":
            continue
            
        linhas_brutas.append(entrada)

    # --- FASE 2: TRANSFORMAÇÃO ---
    dados_limpos = []
    for linha in linhas_brutas:
        try:
            partes = linha.split(',')
            if len(partes) != 4:
                print(f"Linha ignorada (formato errado): {linha}")
                continue
            
            # Limpeza e Conversão (Requisitos da imagem)
            data = partes[0].strip()
            produto = partes[1].strip()
            valor = float(partes[2].strip()) # Converte para float
            estado = partes[3].strip().upper() # Padroniza estado
            
            dados_limpos.append([data, produto, valor, estado])
        except ValueError:
            print(f"Erro de digitação no valor: {linha}")

    if not dados_limpos:
        print("Nenhum dado válido para processar.")
        return

    # --- FASE 3: CARGA E ANÁLISE (Matrizes/DataFrame) ---
    df = pd.DataFrame(dados_limpos, columns=['Data', 'Produto', 'Valor', 'Estado'])

    print("\n--- RESULTADOS DA ANÁLISE ---")
    # Query: Total por estado
    vendas_estado = df.groupby('Estado')['Valor'].sum()
    print(f"Vendas por Estado:\n{vendas_estado}")
    
    # Query: Ticket Médio
    print(f"\nTicket Médio: R$ {df['Valor'].mean():.2f}")

    # --- FASE 4: GRÁFICO DE BARRAS ---
    vendas_estado.plot(kind='bar', color='royalblue', edgecolor='black')
    plt.title('Total de Vendas por Estado')
    plt.ylabel('Valor (R$)')
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    sistema_etl_terminal()