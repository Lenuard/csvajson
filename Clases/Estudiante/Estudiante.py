import os

class Estudiante:
    def __init__(self, estudiante_id, nombre, apellido):
        self.id = estudiante_id
        self.nombre = nombre
        self.apellido = apellido



ruta = 'C:\\Users\\57311\\Desktop\\Tarea3IngSoftware\\estudiantes.csv'
path, filename = os.path.split(ruta)

nombre = os.path.splitext(filename)[0]
json = os.path.join(path, os.path.splitext(filename)[0] + '.json')

print(path, '-----', filename, '------', json, nombre)