class HistoryData:
    column = ['GENERO', 'DNI', 'CUIL']
    history = []

    def __init__(self):
        pass

    def getColumn(self):
        return self.column

    def getHistory(self):
        return self.history
    
    def addHistory(self, element):
        self.history.append(element)
