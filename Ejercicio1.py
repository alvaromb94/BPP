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

#Realizamos suma por columnas
print(np.sum(df, axis=0))
print("\n")

"""
Los meses de Enero, Julio, Septiembre, Octubre y Noviembre contienen carácteres tipo Char que debemos convertir en 0 para poder realizar 
la suma de las columnas de manera correcta
"""

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

#Sumamos columnas      
print(np.sum(df, axis=0))
print("\n")

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
print(f"Enero: {enero}€")
print(f"Febrero: {febrero}€")
print(f"Marzo: {marzo}€")
print(f"Abril: {abril}€")
print(f"Mayo: {mayo}€")
print(f"Junio: {junio}€")
print(f"Julio: {julio}€")
print(f"Agosto: {agosto}€")
print(f"Septiembre: {septiembre}€")
print(f"Octubre: {octubre}€")
print(f"Noviembre: {noviembre}€")
print(f"Diciembre: {diciembre}€")
print("\n")

#Ingreso máximo del año
ingreso_maximo = max(np.sum(df, axis=0))
print(f"El ingreso maximo es {ingreso_maximo}€ \n")

#Gasto máximo del año
gasto_maximo = min(np.sum(df, axis=0))
print(f"El gasto máximo es {gasto_maximo}€ \n")

#Calcular la media de gastos
resultado = [np.sum(df, axis= 0)]
media = (np.sum(resultado))/len(col_list)
print(f"La media de gasto total a lo largo del año es {media}€/mes \n")

#Calcular el gasto total
meses = [enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre]

def gasto_total():
    gasto = 0
    for i in meses:
        if i < 0:
            gasto = gasto + i
        
    return gasto

print(f"El gasto total a lo largo del año es: {gasto_total()}€ \n")

#Calcular el ingreso total
def ingreso_total():
    ingreso = 0
    for i in meses:
        if i > 0:
            ingreso = ingreso + i
    return ingreso

print(f"El ingreso total a lo largo del año es: {ingreso_total()}€ \n")

