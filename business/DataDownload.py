from os import path, getcwd

class DataDownload:
    def __init__(self, data):
        self.data = data

    def write(self):
        pathFile = path.join(getcwd(), 'static', 'result', 'data.txt')
        with open(pathFile, 'w') as file:
            file.write(f'GENERO: {self.data.get('genero')}, DNI: {self.data.get('dni')}, CUIL: {self.data.get('cuil')}')
        return True