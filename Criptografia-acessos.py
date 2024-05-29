from cryptography.fernet import Fernet 
import json
import os
import tkinter as tk

def enviar_login():
    
    usuario= entrada_login.get()
    senha = entrada_senha.get()
    cryptographyRB(usuario,senha)
    
    
    
def cryptographyRB(usuario,senha):
    
    #Gerando a chave da criptografia
    key = Fernet.generate_key() 

    fernet = Fernet(key) 

    #Criptografando Login
    encLogin = fernet.encrypt(usuario.encode())
    #Criptografando Login
    encSenha = fernet.encrypt(senha.encode())

    ##### TRATANDO DADOS ANTES DE GUARDAR ######
    key = str(key)[2:len(str(key))-1]
    encLogin = str(encLogin)[2:len(str(encLogin))-1]
    encSenha = str(encSenha)[2:len(str(encSenha))-1]

    # Dados a serem escritos no arquivo JSON
    dados = {
    "key": str(key),
    "login": str(encLogin),
    "senha": str(encSenha)
    }
    
    
    # Escrever os dados no arquivo JSON
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    nome_arquivo = "acessos.json"
    caminho_arquivo = os.path.join(desktop_path, nome_arquivo)
    print(caminho_arquivo)
    with open(caminho_arquivo, 'w') as file:
        json.dump(dados, file)
        
        
        

# Criando a janela
janela = tk.Tk()
janela.title("Critografia")

largura_pixels = 500
altura_pixels = 250
janela.geometry(f"{largura_pixels}x{altura_pixels}")

# Mudar cor de fundo para azul
janela.configure(bg='blue')

# Título na parte superior da janela
titulo_superior = tk.Label(janela, text="Criptografia de Acessos", font=("Arial", 20),bg='blue',fg='white')
titulo_superior.pack(pady=10)  # Adicionando espaço entre o topo da janela e o título

# Título antes do campo de Login
titulo_login = tk.Label(janela, text="Login:", font=("Arial", 12, "bold"),bg='blue',fg='white')
titulo_login.pack()

# Campo de Login
entrada_login = tk.Entry(janela, font=("Arial", 10))  # Aumentando o tamanho da fonte
entrada_login.pack(padx=10, pady=5)  # Adicionando espaçamento

# Campo de Senha
label_senha = tk.Label(janela, text="Senha:", font=("Arial", 12, "bold"),bg='blue',fg='white')
label_senha.pack()
entrada_senha = tk.Entry(janela, show="*", font=("Arial", 10))  # Para ocultar a senha
entrada_senha.pack(padx=10, pady=5)  # Adicionando espaçamento

# Botão para enviar
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_login, font=("Arial", 12))
botao_enviar.pack(padx=10, pady=5)  # Adicionando espaçamento

# Iniciando a janela
janela.mainloop()