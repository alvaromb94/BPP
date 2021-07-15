import csv
import pandas as pd

df = pd.read_csv("C:/Users/Usuario/OneDrive/Escritorio\MásterPython/4 - BUENAS PRACTICAS DE PROGRAMACION EN PYTHON/LECCIÓN 1. CONTROL DE ERRORES, PRUEBAS Y VALIDACIÓN DE DATOS/ACTIVIDAD/finanzas2020.csv", delimiter="\t")

#Comprobar existencia de fichero
try:
    fichero = open("C:/Users/Usuario/OneDrive/Escritorio\MásterPython/4 - BUENAS PRACTICAS DE PROGRAMACION EN PYTHON/LECCIÓN 1. CONTROL DE ERRORES, PRUEBAS Y VALIDACIÓN DE DATOS/ACTIVIDAD/finanzas2020.csv", "r")
    reader = csv.reader(fichero)
    print(reader)
    

except IOError as err:
    print("No se encuentra el fichero o no se puede leer. Error.", err)

else:   
    print("El fichero se ha podido leer sin problemas \n")


class Error(Exception):
    pass

class valorDemasiadoPequeñoError(Error):
    pass

class valorDemasiadoGrandeError(Error):
    pass


#Comprobar numero de columnas
while(True):
    try:
        columnas = len(list("finanzas.csv"))
        if(columnas < 12):
            raise valorDemasiadoGrandeError
        elif (columnas > 12):
            raise valorDemasiadoPequeñoError
        break

    except valorDemasiadoGrandeError:
        print("El número de columnas del fichero es mayor que 12")
        print("\n")

    except valorDemasiadoPequeñoError:
        print("El número de columnas del fichero es menor que 12")
        print("\n")

print("El fichero tiene 12 columnas. \n")
        

#Comprobar que hay contenido para cada mes
print(df.head)

#Comprobar que los datos son correctos
archivo = list(reader)
dataset = []

for i in range(1, len(archivo)):
    for n in archivo[i]:
        try:
            dato = int(n)
            dataset.append(dato)
        except:
            dato = 0
            dataset.append(dato)

dataset = archivo
print(dataset)