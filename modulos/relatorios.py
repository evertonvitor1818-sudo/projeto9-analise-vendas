def gerar_grafico_vendas(vendas_estado):
    if not vendas_estado:
        print("Nenhum dado para exibir.")
        return

    largura_maxima = 30
    valor_referencia = max(vendas_estado.values())  # corrigido: recebe dict diretamente

    print("\n--- TOTAL DE VENDAS POR ESTADO ---")

    for estado, valor in vendas_estado.items():
        tamanho_barra = int((valor / valor_referencia) * largura_maxima)
        barra = "█" * tamanho_barra
        print(f"{estado:<4} │ {barra} R$ {valor:>5.2f}")

    
    print("     └" + "─" * (largura_maxima + 16))
