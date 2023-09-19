def fragmentar_arquivo(nome_arquivo, num_partes):
    with open(nome_arquivo, 'r') as arquivo:
        # Ler o tamanho total do arquivo
        tamanho_total = os.path.getsize(nome_arquivo)
        
        # Calcular o tamanho aproximado de cada parte
        tamanho_parte = tamanho_total // num_partes

        for i in range(num_partes):
            # Criar o nome do arquivo de saída
            nome_parte = f'NOME_ARQUIVO_PART_{i + 1}.txt'

            with open(nome_parte, 'w') as arquivo_parte:
                bytes_lidos = 0

                while bytes_lidos < tamanho_parte:
                    # Ler uma porção do arquivo
                    buffer = arquivo.read(1024)  # Ler em pedaços de 1KB
                    if not buffer:
                        break

                    # Escrever a porção lida no arquivo de saída
                    arquivo_parte.write(buffer)
                    bytes_lidos += len(buffer)

                # Calcular e exibir a porcentagem de progresso
                progresso = (i + 1) / num_partes * 100
                print(f'Progresso: {progresso:.2f}%')

if __name__ == "__main__":
    import os

    nome_arquivo = input("Digite o nome do arquivo de entrada: ")
    num_partes = int(input("Digite o número de partes desejadas: "))

    fragmentar_arquivo(nome_arquivo, num_partes)
    print(f'O arquivo "{nome_arquivo}" foi fragmentado em {num_partes} partes.')
