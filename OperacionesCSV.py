import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Leemos el archivo Csv
df = pd.read_csv('C:/Users/Usuario/OneDrive/Escritorio/MásterPython/4 - BUENAS PRACTICAS DE PROGRAMACION EN PYTHON\LECCIÓN 1. CONTROL DE ERRORES, PRUEBAS Y VALIDACIÓN DE DATOS/ACTIVIDAD/finanzas2020.csv', delimiter='\t')
print(df)

#Creamos una lista con los headers de las columnas, en este caso los meses del año
col_list = list(df)
print(col_list)
print("\n")

#Convertimos valores char a NaN
df['Enero'] = pd.to_numeric(df['Enero'], errors='coerce')
df['Julio'] = pd.to_numeric(df['Julio'], errors='coerce')
df['Septiembre'] = pd.to_numeric(df['Septiembre'], errors='coerce')
df['Octubre'] = pd.to_numeric(df['Octubre'], errors='coerce')
df['Noviembre'] = pd.to_numeric(df['Noviembre'], errors='coerce')

#Convertimos valores NaN a 0
df['Enero'] = df['Enero'].fillna(0)
df['Julio'] = df['Julio'].fillna(0)
df['Septiembre'] = df['Septiembre'].fillna(0)
df['Octubre'] = df['Octubre'].fillna(0)
df['Noviembre'] = df['Noviembre'].fillna(0)


#Realizamos suma por columnas
def sumarColumnas():
    resultado = np.sum(df, axis=0)
    print(resultado) 
    return resultado   


def ingresoMaximo():
    ingMax = max(np.sum(df, axis=0))
    print(f"El ingreso maximo es {ingMax}€ \n")
    return ingMax


def gastoMaximo():
    gstMax = min(np.sum(df, axis=0))
    print(f"El gasto máximo es {gstMax}€ \n")
    return gstMax


def calMedia():
    resultado = [np.sum(df, axis= 0)]
    media = (np.sum(resultado))/len(col_list)
    print(f"La media de gasto total a lo largo del año es {media}€/mes \n")
    return media

enero = np.sum(df['Enero'], axis=0)
febrero = np.sum(df['Febrero'], axis=0)
marzo = np.sum(df['Marzo'], axis=0)
abril = np.sum(df['Abril'], axis=0)
mayo = np.sum(df['Mayo'], axis=0)
junio = np.sum(df['Junio'], axis=0)
julio = np.sum(df['Julio'], axis=0)
agosto = np.sum(df['Agosto'], axis=0)
septiembre = np.sum(df['Septiembre'], axis=0)
octubre = np.sum(df['Octubre'], axis=0)
noviembre = np.sum(df['Noviembre'], axis=0)
diciembre = np.sum(df['Diciembre'], axis=0)
meses = [enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre]

def gasto_total():
    gasto = 0
    for i in meses:
        if i < 0:
            gasto = gasto + i
    print(f"El gasto total a lo largo del año es: {gasto}€ \n")
    return gasto


def ingreso_total():
    ingreso = 0
    for i in meses:
        if i > 0:
            ingreso = ingreso + i
    print(f"El ingreso total a lo largo del año es: {ingreso}€ \n")
    return ingreso



sumarColumnas()
ingresoMaximo()
gastoMaximo()
calMedia()
gasto_total()
ingreso_total()