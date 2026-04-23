def limpezaDosDados(entrada):
    try:
        partes = entrada.split(',')
        if len(partes) != 4:
            print(f"Linha ignorada (formato errado): {entrada}")
            return None
        
        data    = partes[0].strip()
        produto = partes[1].strip()
        valor   = float(partes[2].strip())
        estado  = partes[3].strip().upper()
        
        return (data, produto, valor, estado)
    
    except ValueError:
        print(f"Erro de digitação no valor: {entrada}")
        return None

    