import os
import forca
import advinhacao

os.system('cls')

def escolhe_jogo():
    print("*******************************")
    print("         Escolha o jogo        ")
    print("******************************* \n")

    print(' (1) Forca (2) Advinhação\n')

    jogo = int(input("Qual jogo: "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogo_forca()
    elif(jogo == 2):
        print("Jogando jogo advinhação")
        advinhacao.jogo_advinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()
