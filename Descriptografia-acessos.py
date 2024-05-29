import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet 
import json

def importar_arquivo():
    global login, senha
    arquivo = filedialog.askopenfilename()
    if arquivo:
        campo_arquivo.delete(0, tk.END)
        campo_arquivo.insert(0, arquivo)
        login, senha = descriptography(arquivo)
        
        

def mostrar_resultado():
    campo_resultado.delete(0, tk.END)
    campo_resultado.insert(0, login)
    campo_resultado2.delete(0, tk.END)
    campo_resultado2.insert(0, senha)
    
def descriptography(arquivo):
    try:
        
        with open(arquivo, 'r') as file:
            acessos = json.load(file)
        
        key = str(acessos['key'])
        login = str(acessos['login'])
        senha = str(acessos['senha'])  
        
        fernet = Fernet(bytes(key.encode())) 
        
        decLogin = str(fernet.decrypt(login.encode()))
        decLogin = decLogin[2:len(decLogin)-1]
        decSenha = str(fernet.decrypt(senha.encode()))
        decSenha = decSenha[2:len(decSenha)-1]
        
        return decLogin, decSenha
    except:
        decLogin = "Não foi possivel descriptografar arquivo!"
        decSenha = "Não foi possivel descriptografar arquivo!"
        return decLogin, decSenha
        

# Criando a janela
janela = tk.Tk()
janela.title("Formulário de Acesso")
janela.geometry("500x350")
janela.configure(bg='#f17ea1')

# Título grande em negrito com espaçamento
titulo_grande = tk.Label(janela, text="Descritografar Acesso", font=("Arial", 20, "bold"), fg="white", bg='#f17ea1')
titulo_grande.pack(pady=10)

# Título do campo de arquivo
label_arquivo = tk.Label(janela, text="Selecionar Arquivo:", font=("Arial", 12, "bold"), fg="white", bg='#f17ea1')
label_arquivo.pack()
campo_arquivo = tk.Entry(janela, width=60)  # Aumentando o comprimento do campo de arquivo
campo_arquivo.pack(pady=5)

# Botão para importar arquivo
botao_importar = tk.Button(janela, text=" Importar Arquivo ", command=importar_arquivo)
botao_importar.pack(pady=5)

# Botão para mostrar os resultados
botao_mostrar = tk.Button(janela, text="Mostrar Resultado", command=mostrar_resultado)
botao_mostrar.pack(pady=10)

# Campos para apresentar e copiar os resultados
label_resultado = tk.Label(janela, text="Login", font=("Arial", 12, "bold"), fg="white", bg='#f17ea1')
label_resultado.pack()
campo_resultado = tk.Entry(janela, font=("Arial", 10), width=50)
campo_resultado.pack(pady=5)

label_resultado2 = tk.Label(janela, text="Senha", font=("Arial", 12, "bold"), fg="white", bg='#f17ea1')
label_resultado2.pack()
campo_resultado2 = tk.Entry(janela, font=("Arial", 10), width=50)
campo_resultado2.pack(pady=5)

# Adiciona a funcionalidade de seleção dos resultados
campo_resultado.bind("<FocusIn>", lambda event: campo_resultado.select_range(0, tk.END))
campo_resultado2.bind("<FocusIn>", lambda event: campo_resultado2.select_range(0, tk.END))

# Iniciando a janela
janela.mainloop()
