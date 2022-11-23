'''
# Tema:  Examen 2 segunda Oportunidad
# Fecha: 23/11/2022
# Autor: Juan Antonio Jaramillo Moreno
'''

import json

contactos = [
("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
("Javier", "analista de datos", "javier@ejemplo.com"),
("Marta", "Experta en Python", "marta@ejemplo.com"),
]

lista = []
for datos in contactos:
    directorio = {}
    directorio["nombre"] = datos[0]
    directorio["funcion"] = datos[1]
    directorio["correo"] = datos[2]
    lista.append(directorio)
retornoList = json.dumps(lista)

try:
    with open("examen_json", 'w') as archivo:
        json.dump(lista, archivo)
except Exception as error:
    print("ERROR: ", error)

def json():
    archivo = open('examen_json', 'r')
    cadena = archivo.read()
    archivo.close()
    return cadena

print(json())

