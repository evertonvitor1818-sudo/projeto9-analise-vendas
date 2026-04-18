import matplotlib.pyplot as plt

def gerar_grafico_vendas(vendas_estado):

    vendas_estador.plot(kind='bar', color='royalblue', edgecolor='black')
    plt.title('Total de Vendas por Estado')
    plt.ylabel('Valor (R$)')
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

if _name_ == "_main_":
   