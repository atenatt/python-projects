import os
import random

def limpa_tela():
    os.system('cls')

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

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def define_chute_jogador():
    chute = input("\nDigite sua letra: ").strip().upper()
    return chute

def imprime_mensagem_vencedor(palavra_secreta):
    limpa_tela()
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ") 
  
def imprime_mensagem_perdedor(palavra_secreta):
    limpa_tela()
    print("Você foi enforcado!")
    print(f'A palavra era: {palavra_secreta}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           \n")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        limpa_tela()
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        limpa_tela()
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        limpa_tela()
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        limpa_tela()
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        limpa_tela()
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        limpa_tela()
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        limpa_tela()
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogo_forca():
    limpa_tela()
    
    msg_abertura()

    palavra_secreta = define_palavra_secreta()
    
    letras_acertadas = define_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0
    
    print(f'{letras_acertadas}')

    while(not enforcou and not acertou):
        
        chute = define_chute_jogador()
        
        if (chute in palavra_secreta):    
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
            
        print(f'{letras_acertadas}')
    
    if (acertou):
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)

if(__name__ == "__main__"):    
    jogo_forca()
