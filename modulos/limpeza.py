
def carregar_analytics(produto, valor_unitario, quantidade):
    valor = float(valor_unitario)
    quantidade_int = int(quantidade)
    total = valor * quantidade_int

    print("Produto:", produto)
    print("Total: R$", total)


def limpeza_dos_dados(entrada):
    resultado = []  # acumula todas as linhas válidas

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

    return resultado  # retorna todas as linhas processadas


dados = []

while True:
    entrada = input("Próxima linha: ")

    if entrada.upper() == 'FIM':
        break

    if entrada.strip() == "":
        continue

    dados.append(entrada)  # append modifica a lista no lugar, não retorna nada

linhas_processadas = limpeza_dos_dados(dados)  # passa a lista correta

for data, produto, quantidade, valor_unitario, estado in linhas_processadas:
    carregar_analytics(produto, valor_unitario, quantidade)

