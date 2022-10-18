class Disco:
    def __init__(self, nmrDiscos):
        self._nmrDiscos = nmrDiscos
        self._discos = []
        for x in range(self._nmrDiscos):
            self._discos.append(x+1)

    def getDiscos(self):
        return self._discos

    def discoTopo(self):
        return self._discos[0]

    def qtdDiscos(self):
        return self._nmrDiscos

    def mostrarDiscos(self):
        print('\n___Discos___')
        for x in range(self._nmrDiscos):

            print('Disco Nmrº {}'.format(x+1))