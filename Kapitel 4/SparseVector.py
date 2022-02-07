class SparseVector:
    def __init__(self):
        self.__vector = {}

    def __getitem__(self, index):
        try:
            element = self.__vector[index]
        except:
            return 0.0
        else:
            return element

    def __setitem__(self,index,value):
        self.__vector[index] = value

sv = SparseVector()

sv[12] = 534.4
sv[24] = 3.333
sv[177] = 111.111

for i in range(1,200):
    print(sv[i])
