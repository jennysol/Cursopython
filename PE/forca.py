'''
Descrição:
1.	Fazer um programa com um menu principal onde o usuário poderá escolher três opções:
•	G - Gravar Palavras do Jogo
•	J - Jogar
•	S - Sair
'''

import time
import random

#1
def Menu():
    print('-.-' * 30)
    print('1- Gravar palavras do Jogo')
    print('2- Jogar')
    print('S- Sair')
    escolha = str(input('Digite um número de sua escolha: '))

    if escolha == 'S':
        print('Programa Encerrado.')
    
    if escolha == '1':
        Gravar()

    if escolha == '2':
        Jogar()

# G
def Gravar():
    nome_arquivo = "./palavras.txt"
    arquivo = open(nome_arquivo, "r")

    lista = arquivo.readlines()
    print(f'As palavras adicionadas na lista são: \n{lista}')

    arquivo = open(nome_arquivo, "w")
    conteudo_user = str(input('Digite [S/Sair] para sair \n ou \nGrave sua palavra: '))

    if conteudo_user in lista:
        print('Esta palavra já existe na lista!')
        Menu()

    elif conteudo_user != 'Sair': 
        arquivo.write(conteudo_user)
        print('Palavra gravada com sucesso!')
        Menu()

    if conteudo_user == 'Sair':
        print('Redirecionando para o Menu...')
        time.sleep(1)
        Menu()

def Jogar():
    nome_arquivo = "./palavras.txt"
    arquivo = open(nome_arquivo, "r")

    lista = arquivo.readlines()
    sorteio = random.choice(lista)
    letras_acertadas =  ['_']
    letras_acertadas = letras_acertadas * (sorteio.__len__() -1)

    print(sorteio)
    print(letras_acertadas)


    tentativas = 4

    while tentativas > 0:
        chute = str(input('Digite uma letra: '))
        tentativas -= 0

        achou = False

        for letra in sorteio:
            if chute.upper() == letra.upper():
                achou = True

        if achou == False:
            tentativas = tentativas -1
            print(f'Não tem a letra {chute}...')
            print('Ainda faltam %d tentativas\n' %tentativas)

        print(f'Tentativas computadas {chute}')

        if achou == True:
            


Menu()