import os
import random

def msg_abertura():
    
    print("*******************************")
    print("    Bem vindo ao jogo forca    ")
    print("******************************* \n")

def define_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)   
        
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def define_letras_acertadas(palavra):
    return ["_" for letra in palavra]
    

def jogo_forca():
    os.system('cls')
    
    msg_abertura()

    palavra_secreta = define_palavra_secreta()
    
    letras_acertadas = define_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0
    
    print(f'{letras_acertadas}')

    while(not enforcou and not acertou):
        
        chute = input("\nDigite sua letra: ").strip().upper()
        #chute = chute.strip().upper()
        
        if (chute in palavra_secreta):    
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
            
        print(f'{letras_acertadas}')
    
    if (acertou):
        os.system('cls')
        print(f'Você ganhou, a palavra secreta era: {palavra_secreta.lower()}')
        
    else:
        print('Você perdeu...')
    
    print("\nFim de jogo")

if(__name__ == "__main__"):    
    jogo_forca()
