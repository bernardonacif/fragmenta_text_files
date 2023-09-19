def fragmentar_arquivo(nome_arquivo, num_partes):
    with open(nome_arquivo, 'r') as arquivo:
        # Ler o conteúdo do arquivo em uma lista de linhas
        linhas = arquivo.readlines()

        # Calcular o número de linhas por parte
        num_linhas_por_parte = len(linhas) // num_partes

        for i in range(num_partes):
            # Calcular os índices de início e fim para cada parte
            inicio = i * num_linhas_por_parte
            fim = (i + 1) * num_linhas_por_parte if i < num_partes - 1 else len(linhas)

            # Criar o nome do arquivo de saída
            nome_parte = f'NOME_ARQUIVO_PART_{i + 1}.txt'

            with open(nome_parte, 'w') as arquivo_parte:
                # Escrever as linhas da parte atual no arquivo de saída
                arquivo_parte.writelines(linhas[inicio:fim])

            # Calcular e exibir a porcentagem de progresso
            progresso = (i + 1) / num_partes * 100
            print(f'Progresso: {progresso:.2f}%')

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    num_partes = int(input("Digite o número de partes desejadas: "))

    fragmentar_arquivo(nome_arquivo, num_partes)
    print(f'O arquivo "{nome_arquivo}" foi fragmentado em {num_partes} partes, preservando a integridade das linhas.')
