from Clases.Estudiante.Estudiante import Estudiante
import csv
import json
import os


class Archivo:
    def __init__(self, ruta):
        self.ruta = ruta

    #Este metodo lee el archivo csv, con los datos del archivo crea estudiantes y los agrega a un arreglo
    #y retorna el arreglo
    def leer_estudiantes(self):
        estudiantes = []
        with open(self.ruta, 'r', encoding='utf-8') as file:
            CSV = csv.reader(file)
            for i in CSV:
                estudiante = Estudiante(i[0], i[1], i[2])
                estudiantes.append(estudiante)
        return estudiantes

    #Este metodo separa la ruta en dos, tomando la ruta donde esta el archivo y el nombre del archivo
    # y los pone en variables separadas, luego con esta informacion crea una nueva ruta que sera el json
    #luego recorre el arreglo de estudiantes y mete los datos en una variable 'datos' que sera la ifnormacion que se
    # insertara en el archivo json
    def escribir_estudiantes(self, estudiantes):
        ruta_archivo, nombre_archivo = os.path.split(self.ruta)
        archivo_json = os.path.join(ruta_archivo, os.path.splitext(nombre_archivo)[0] + '.json')
        datos = []
        for estudiante in estudiantes:
            datos.append({
                'id': estudiante.id,
                'nombre': estudiante.nombre,
                'apellido': estudiante.apellido
            })
        with open(archivo_json, 'w', encoding='utf-8') as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)
        print('Archivo JSON creado: ', datos)


ruta = input('Ingrese la ruta completa del archivo: ')
archivo = Archivo(ruta)

if os.path.isfile(ruta):
    estudiantes = archivo.leer_estudiantes()
    archivo.escribir_estudiantes(estudiantes)

else:
    print('No se encuentra el archivo')
