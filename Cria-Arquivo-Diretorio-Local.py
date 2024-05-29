import os

# Obtém o caminho do diretório do desktop do usuário
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# Define o conteúdo do arquivo
conteudo_arquivo = "Este é o conteúdo do arquivo que será salvo no desktop."

# Define o caminho completo do arquivo (neste exemplo, será um arquivo de texto)
nome_arquivo = "arquivo_no_desktop.txt"
caminho_arquivo = os.path.join(desktop_path, nome_arquivo)

# Escreve o conteúdo no arquivo
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write(conteudo_arquivo)

print(f"Arquivo salvo em: {caminho_arquivo}")
