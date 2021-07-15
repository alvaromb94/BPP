import pytest
import OperacionesCSV
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/Usuario/OneDrive/Escritorio/MásterPython/4 - BUENAS PRACTICAS DE PROGRAMACION EN PYTHON\LECCIÓN 1. CONTROL DE ERRORES, PRUEBAS Y VALIDACIÓN DE DATOS/ACTIVIDAD/finanzas2020.csv', delimiter='\t')
lista = df.columns

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

resultado = np.sum(df, axis=0)

"""def test_sumar_col():
    suma = np.sum(df, axis=0)
    assert suma == OperacionesCSV.sumarColumnas()"""

def test_ing_max():
    ing_max = max(np.sum(df, axis=0))
    assert ing_max == OperacionesCSV.ingresoMaximo()

def test_gast_max():
    gst_max = min(np.sum(df, axis=0))
    assert gst_max == OperacionesCSV.gastoMaximo()

def test_media():
    med = (np.sum(resultado))/len(lista)
    assert med == OperacionesCSV.calMedia()


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

def test_gasto_tot():
    gasto = 0
    for i in meses:
        if i < 0:
            gasto = gasto + i
    assert gasto == OperacionesCSV.gasto_total()

def test_ing_tot():
    ing = 0
    for i in meses:
        if i > 0:
            ing = ing + i
    assert ing == OperacionesCSV.ingreso_total()
    

