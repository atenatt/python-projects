import os                                                           # Importando o cls para limpar tela.

os.system('cls')                                                    # Limpando a tela pra perguntar a palavra secreta
palavra_secreta = input('Digite a palavra secreta: ')               # Perguntando a palavra secreta
os.system('cls')                                                    # Limpando a tela para iniciar o game
letras_acertadas = ''                                               # Variavel das letras acertadas zerado
tentativas = 0                                                      # Quantidade de tentativas zerado

while True:                                                         # Criando um loop para o game
    tentativas += 1                                                 # Adicionando mais um na variavel de tentativa
    letra_digitada= input('Digite uma letra: ')                     # Recebendo o input da letra.
    if letra_digitada.isalpha():                                    # Validando se o input é uma letra.
        if len(letra_digitada) > 1:                                 # Validando se é apenas uma letra.
            print('Digite apenas uma letra.')                       # Exibindo que é mais de uma letra
            continue                                                # Reiniciando o Loop
        
        if letra_digitada in palavra_secreta:                       # Verificando se a letra digitada pertence a palavra secreta
            letras_acertadas += letra_digitada                      # Se pertencer então ele concatenará numa variavel nova.
            
        palavra_formada = ''                                        # Criando uma variavel para a palavra se formando
        for i in palavra_secreta:                                   # Verifica as letras da palavra secreta
            if i in letras_acertadas:                               # Se a letra da palavra secreta estiver na palavra formada então
#                                                                   A palavra formada receberá o seu valor.
                palavra_formada += i                                # Palavra formada recebendo o valor da palavra secreta
            else:                                                   # Se não estiver ele receberá o * no lugar
                palavra_formada += '*'                              # Recebendo o * invés da letra correta
        print(palavra_formada)                                      # Exibindo o resultado.
        
        if palavra_formada == palavra_secreta:                      # Verificando a palavra formada é igual a palavra secreta
            os.system('cls')                                        # Caso seja limpará a tela
            print(f'Voce acertou! a palavra secreta era "{palavra_secreta}"')   # Printando a mensagem de sucesso
            print(f'Voce tentou: {tentativas} vezes\n')             # Printando as tentativas do usuário
            exit = 0                                                # Definindo uma flag com valor 1 para o loop de sair             
        while exit == 0:                                            # Enquanto a flag for 1 ele irá executar isso
            
            print('Deseja jogar novamente com a mesma palavra?')    # Questionando o usuario se deseja jogar com a mesma palavra
            sair = input('[s]im / [n]ao: ')                         # Recebendo a decisão do usuario em sair ou continuar
            if sair == 'n' or sair == 'N':                          # Caso o usuario digite que n ou N para sair
                os.system('cls')                                    # Limpando a tela
                exit = 2                                            # Aplicando um valor de 2 para sair do loop
                break                                               # Saindo do programa
            elif sair == 's' or sair == 'S':                        # Caso ele digite outra coisa
                os.system('cls')                                    # Limpando a tela para sair
                letras_acertadas = ''                               # Zerando a palavra acertada para caso ele continue
                tentativas = 0                                      # Zerando as tentativas para caso ele continue 
                exit = 1                                            # Aplicando um valor 0 para sair do loop
            else:                                                   # Caso a flag nao altere nenhum valor continuara o loop
                os.system('cls')                                    # Limpando a tela
                continue                                            # Iniciando o loop de sair
        if exit == 2:                                               # Se a flag for 2 (Definida com o sair) entao sairá do programa
            break                                                   # Exit do programa
        elif exit == 1:                                             # Se nao for 2 então reiniciará o programa
            continue                                                # Reiniciando o programa
            
    else:                                                           # Caso usuario nao digite uma letra
        print('Voce não digitou uma letra')                         # Printando o erro
        continue                                                    # Reiniciando o loop