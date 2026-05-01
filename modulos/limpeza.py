def limpeza_dos_dados(entrada):
    resultado = []

    for linha in entrada:
        try:
            partes = linha.split(',')

            if len(partes) != 5:
                print(f"Linha ignorada (formato errado): {linha}")
                continue

            data           = partes[0].strip()
            produto        = partes[1].strip()
            quantidade     = int(partes[2].strip())
            valor_unitario = float(partes[3].strip().replace(',', '.'))
            estado         = partes[4].strip().upper()

            resultado.append((data, produto, quantidade, valor_unitario, estado))

        except ValueError:
            print(f"Erro de digitação no valor: {linha}")
            continue

    return resultado
