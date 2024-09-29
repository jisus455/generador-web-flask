class DataDownload:
    def __init__(self, data):
        self.data = data

    def write(self):
        with open('./static/result/data.txt', 'w') as file:
            file.write(f'GENERO: {self.data.get('genero')}, DNI: {self.data.get('dni')}, CUIL: {self.data.get('cuil')}')
        return True