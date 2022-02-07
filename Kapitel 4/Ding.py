class Ding:
    _dichte = {'Au':('Gold',19.32),
            'Ag':('Silber',10.5),
            'Fe':('Eisen',7.87)}

    def __init__(self, symbol, volumen):
        self.__volumen = float(volumen)
        self._symbol = symbol

    def getMasse(self):
        return self.__volumen * self._dichte[self._symbol][1]
    def getVolumen(self):
        return self.__volumen

    def __str__(self):
        return 'Das Ding besteht aus ' + self._dichte[self._symbol][0] + ', hat ein Volumen von ' + format(self.getVolumen(),'.2f') + ' ccm und hat eine Masse von ' + format(self.getMasse(), '.2f') + ' g.'

ding = Ding('Au', 100)
print(ding)
