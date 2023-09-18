import os
import random

def jogo_advinhacao():
    os.system('cls')

    print("*******************************")
    print("Bem vindo no jogo de advinhação")
    print("******************************* \n")

    numero_secreto = random.randrange(1, (100 + 1))
    total_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade? ')
    print('(1) Fácil (2) Médio (3) Difícil (4) Ninja\n')

    nivel = int(input("Defina o nível: "))
    os.system('cls')

    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 5
    elif(nivel == 3):
        total_tentativas = 3
    else:
        total_tentativas = 1

    for rodada in range(1, total_tentativas + 1):
        print(f'\nTentativa [{rodada}] de {total_tentativas}\n')
        chute = input("Digite um número: ")
        chute = int(chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            os.system('cls')
            print(f'Você acertou e fez {pontos} pontos!')
            break
        else:
            if(maior):
                os.system('cls')
                print("\nVocê errou! seu chute foi maior que o número secreto")
            elif(menor):
                os.system('cls')
                print("\nVocê errou! seu chute foi menor que o número secreto")
            pontos_perdidos = abs((numero_secreto - chute))
            pontos = pontos - pontos_perdidos

        #rodada = rodada + 1

    print(f'O número secreto era: {numero_secreto}')
    print ("\nFim do jogo")

if(__name__ == "__main__"):    
    jogo_advinhacao()