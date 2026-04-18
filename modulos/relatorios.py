import matplotlib.pyplot as plt

def gerar_grafico_vendas(vendas_estado):

    vendas_estado.plot(kind='bar', color='royalblue', edgecolor='black')
    plt.title('Total de Vendas por Estado')
    plt.ylabel('Valor (R$)')
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Exemplo de uso
    vendas_estado = {
        'SP': 150000,
        'RJ': 120000,
        'MG': 90000,
        'RS': 60000,
        'BA': 30000
    }
    gerar_grafico_vendas(vendas_estado)