import streamlit as st
from streamlit_lottie import st_lottie
import requests

def introduccion():
    # Definimos un tÍtulo y subtítulo general para la página.
    st.header("MODELOS DE PREDICCIÓN DE SERIES TEMPORALES")
    st.markdown("##### Usamos distintos modelos para predecir diferentes variables del sistema electrico español")

    st.title('INTRODUCCIÓN')
    st_lottie(requests.get("https://lottie.host/8aa6eb40-cc19-4c8a-82e8-65abc765569a/VlL8VDrMsa.json").json(), height=250, key="Into1")
    
    st.write('<div style="text-align: justify;">El objeto del siguiente proyecto es usar los diversos datos obtenidos de la API de red \
            eléctrica para predecir datos futuros usando distintos modelos (SKForecast, Redes Neuronales, Prophet y Pycaret). \
            Los datos actuales de demanda y precios nos servirán para \
            entrenar un modelo de redes neuronales que nos permitirá predecir estas variables en un \
            rango de tiempo determinado. Para lograr esto usamos modelos que \
            funcionen bien con predicción de variables en series temporales, como SKForest, Redes Neuronales, Pycaret y Prophet. \
            En esta presentación web de Streamlit podréis navegar en el menú y ver como se realiza \
            cada modelo y los resultados obtenidos del mismo, como norma general obtendremos un \
            gráfico de predicción y unos valores de precisión del modelo que nos dirán cuán bueno es el \
            mismo \
                \
                .</div>', unsafe_allow_html=True)
    
    

if __name__ == "__introduccion__":
    introduccion()