import pandas as pd

def limpezaDosDados(entrada):

    linhas_brutas = [] 
    dados_limpos = []
    linhas_brutas.append(entrada)
    
    for linha in linhas_brutas:
        try:
            partes = linha.split(',')
            if len(partes) != 4:
                print(f"Linha ignorada (formato errado): {linha}")
                continue
            
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

    