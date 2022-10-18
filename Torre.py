class Torre:

    # 'letraTorre', string para representar a ordem das torres. ex: 'A, B, C'.
    # 'discos', array que conterá os discos das torres.
    def __init__(self, letraTorre):
        self._letraTorres = letraTorre
        self._discosTorre = []

    def inicializarTorre(self, discos):
        for x in discos:
            self._discosTorre.append(x)

    def mostrarTorre(self):
        
        for i in range(len(self._discosTorre)):
            print(' _-{}-_ '.format(self._discosTorre[i]))
            
    def discoTopoTorre(self):
        return self._discosTorre[0]

    def tamanhoTorre(self):
        return len(self._discosTorre)

    def addDisco(self, discoTopo):
        self._discosTorre.insert(0, discoTopo)
    
    def transferirDisco(self, torre, discoTopo):
        if torre._discosTorre == []:
            torre.addDisco(discoTopo)
            self._discosTorre.remove(self._discosTorre[0])
        
        else:            
            if discoTopo < torre._discosTorre[0]:
                torre.addDisco(discoTopo)
                self._discosTorre.remove(self._discosTorre[0])

            else:
                print('\n**Não é possível fazer a transferência, discos maiores não podem ficar acima de discos menores**')
                input('\nPressione qualquer tecla para continuar.')
