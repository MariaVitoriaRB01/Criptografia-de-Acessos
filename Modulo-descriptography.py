from cryptography.fernet import Fernet 
import json

def main():
    
    try:
        
        with open('acessos.json', 'r') as file:
            acessos = json.load(file)
        
        key = str(acessos['key'])
        login = str(acessos['login'])
        senha = str(acessos['senha'])  
        
        fernet = Fernet(bytes(key.encode())) 
        
        decLogin = str(fernet.decrypt(login.encode()))
        decLogin = decLogin[2:len(decLogin)-1]
        decSenha = str(fernet.decrypt(senha.encode()))
        decSenha = decSenha[2:len(decSenha)-1]
        
        print("decrypted LOGIN: ", decLogin)
        print("decrypted SENHA: ", decSenha)
        
        ''
    except:
        print("Arquivo não existe!")
        temArquivo = False
    

if  __name__ == '__main__':
    main()
