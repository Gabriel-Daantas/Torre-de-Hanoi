from Disco import Disco
from Torre import Torre
import os

clear = lambda: os.system('cls')

def bemVindo():
    clear()
    print('### Bem vindo ###\n')
    print('Regras:\n* Mova os discos 1 à 1 até formar a torre C completa.\n* Os discos maiores não podem ficar em cima dos discos menores.')
    input('\nPressione qualquer tecla para continuar.')

def criarDiscos():
    clear()
    nmr_discos = int(input('*Minimo de 3 discos.\n*Máximo de 8 discos\nCom quantos discos deseja jogar? '))
    
    if nmr_discos < 3 or nmr_discos > 8:
        clear()
        print('ERRO, VALOR INDISPONÍVEL!')
        input('\nPressione qualquer tecla para continuar.')
        criarDiscos()
    else:
        global discos
        discos = Disco(nmr_discos)

def criarTorres():
    global torreA
    global torreB
    global torreC
    torreA = Torre('A')
    torreB = Torre('B')
    torreC = Torre('C')

def iniciarTorre():
    torreA.inicializarTorre(discos.getDiscos())

def desenhoTorres():
    clear()
    print('\nTorre A\n')
    torreA.mostrarTorre()
    
    print('\nTorre B\n')
    torreB.mostrarTorre()
    
    print('\nTorre C\n')
    torreC.mostrarTorre()

def escolhaDeDiscosETorres():
    desenhoTorres()
    global torre_retirar
    global torre_adicionar
    torre_retirar = input('De qual Torre deseja retirar o disco? ')
    if torre_retirar != 'A' and torre_retirar != 'B' and torre_retirar != 'C':
        print('\nERRO, VALOR INDISPONÍVEL!')
        input('\nPressione qualquer tecla para continuar.')
        escolhaDeDiscosETorres()
    else:
        torre_adicionar = input('Para qual torre deseja transferir o disco? ')
        if torre_adicionar != 'A' and torre_adicionar != 'B' and torre_adicionar != 'C':
            print('\nERRO, VALOR INDISPONÍVEL!')
            input('\nPressione qualquer tecla para continuar.')
            escolhaDeDiscosETorres()
        else:
            trocarDiscoDeTorre()

def trocarDiscoDeTorre():
    if torre_retirar == 'A':
        if torre_adicionar == 'B':
            torreA.transferirDisco(torreB, torreA.discoTopoTorre())
        if torre_adicionar == 'C':
            torreA.transferirDisco(torreC, torreA.discoTopoTorre())
    
    if torre_retirar == 'B':
        if torre_adicionar == 'A':
            torreB.transferirDisco(torreA, torreB.discoTopoTorre())
        if torre_adicionar == 'C':
            torreB.transferirDisco(torreC, torreB.discoTopoTorre())
    
    if torre_retirar == 'C':
        if torre_adicionar == 'A':
            torreC.transferirDisco(torreA, torreC.discoTopoTorre())
        if torre_adicionar == 'B':
            torreC.transferirDisco(torreB, torreC.discoTopoTorre())

def finalizarJogo():
    clear()
    desenhoTorres()
    print('\nParabéns, completou o Objetivo.')

def jogo():
    criarDiscos()
    criarTorres()
    iniciarTorre()
    while (torreC.tamanhoTorre() != discos._nmrDiscos):
        escolhaDeDiscosETorres()
    


def testes():
    print(discos.discoTopo())