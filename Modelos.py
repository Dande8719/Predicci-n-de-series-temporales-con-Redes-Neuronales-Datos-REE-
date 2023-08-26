
import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px
#from sktime.utils.plotting import plot_series
import datetime
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
#from sklearn.linear_model import Perceptron
#from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.models import load_model
#from keras.models import Sequential
#from keras.layers import Input, SimpleRNN, Dense, Flatten
#import tensorflow as tf
#from sklearn.preprocessing import MinMaxScaler
import requests
import json
import numpy as np

df_demanda_nacional = pd.read_csv('DF/demanda_nacional.csv')


def Modelos():
    st.title('MODELOS DE PREDICCIÓN')
        #Texto
    st.write('A Continuación seleccionamos entre las distintas variables a predecir para ver los resultados  \
                  de los modelos que usamos para la predicción de las mismas.')

    opcion = st.selectbox('Seleccione una opción', ['DEMANDA','PRECIOS'])

        #Opcione de predicción por generación 
    if opcion == 'DEMANDA':
        st.title('DEMANDA')

        st.write('Obtenemos los datos de demanda eléctrica nacional de la API de Red eléctrica de España, los \
                 pasamos a GW/h y obtenemos una serie temporal de datos de 11 años de energía eléctrica \
                 consumida en España con valores diarios. Aqui podemos ver la predición de valores futuros con distintos modelos, \
                 Hagan click por favor en los botones que ven abajo para ver el resultado de los mismos') 
        col1, col2, col3,COL4 = st.columns([1, 1, 1, 1])

            #Creamos una serie de botones para seleccionar el tipo de modelo a aplicar.
        if col1.button("Modelo Pycaret", key="Pycaret"):
            st.write("Usamos el Modelo Pycaret para predecir series temporales .......")
                
        if col2.button("Modelo Prophet", key="Modelo prophet"):
                 st.write("¡Has hecho clic en el Modelo Prophet!")

        if col3.button("REDES NEURONALES", key="REDES NEURONALES"):
            st.write("¡Has hecho clic en el Modelo REDES NEURONALES La predicción tardará unos minutos, ten paciencia")

        if COL4.button("SKForecast", key="SKForecast"):
            st.write("¡Has hecho clic en el Modelo SKForecast La predicción tardará unos minutos, ten paciencia")    



        
    if opcion == 'PRECIOS':
        st.title('PRECIOS')

        st.write('Obtenemos los datos de precios del mercado electrico de la API de Red eléctrica de España \
                 y obtenemos una serie temporal de datos de 8 años de precios \
                 del mercado electrico en España, valores diarios en €/Mwh.')
            #Creamos una serie de botones para seleccionar el tipo de modelo a aplicar.
        col1, col2, col3 = st.columns([1, 1, 1])
        if col1.button("Modelo Pycaret", key="Pycaret"):
                 st.write("Usamos el Modelo Pycaret para predecir series temporales .......")

        if col2.button("Modelo Prophet", key="Modelo prophet"):
                 st.write("¡Has hecho clic en el Modelo Prophet!")

        if col3.button("REDES NEURONALES", key="REDES NEURONALES"):
                 st.write("¡Has hecho clic en el Modelo X")
    

if __name__ == "__Modelos__":
    Modelos()
