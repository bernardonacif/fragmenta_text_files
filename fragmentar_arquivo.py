def fragmentar_arquivo(nome_arquivo, num_partes):
    # Ler o conteúdo do arquivo de entrada
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

    # Calcular o tamanho aproximado de cada parte
    tamanho_parte = len(conteudo) // num_partes

    for i in range(num_partes):
        # Calcular os índices de início e fim para cada parte
        inicio = i * tamanho_parte
        fim = (i + 1) * tamanho_parte if i < num_partes - 1 else len(conteudo)

        # Extrair a parte atual
        parte = conteudo[inicio:fim]

        # Criar o nome do arquivo de saída
        nome_parte = f'NOME_ARQUIVO_PART_{i + 1}.txt'

        # Escrever a parte em um novo arquivo
        with open(nome_parte, 'w') as arquivo_parte:
            arquivo_parte.write(parte)

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    num_partes = int(input("Digite o número de partes desejadas: "))

    fragmentar_arquivo(nome_arquivo, num_partes)
    print(f'O arquivo "{nome_arquivo}" foi fragmentado em {num_partes} partes.')
