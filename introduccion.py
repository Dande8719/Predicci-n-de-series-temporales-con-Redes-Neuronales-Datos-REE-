import streamlit as st

def introduccion():
    st.title('INTRODUCCIÓN')
    st.write('<div style="text-align: justify;">El objeto del siguiente proyecto es usar los diversos datos obtenidos de la API de red \
            eléctrica para predecir datos futuros usando redes neuronales. \
            Los datos actuales de demanda, generación, precios e intercambio nos servirán para \
            entrenar un modelo de redes neuronales que nos permitirá predecir estas variables en un \
            rango de tiempo determinado. Para lograr esto usamos modelos de redes neuronales que \
            funcionen bien con predicción de variables en series temporales, como las redes neuronales \
            con recursividad. \
            En esta presentación web de Streamlit podréis navegar en el menú y ver como se realiza \
            cada modelo y los resultados obtenidos del mismo, como norma general obtendremos un \
            gráfico de predicción y unos valores de precisión del modelo que nos dirán cuán bueno es el \
            mismo \
                \
                .</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 2, 2])
    col1.image("Foto/Prophet.JPG", use_column_width = True,)
    col2.image("Foto/Redes_Neuronales.JPG", use_column_width = True,)
    col3.image("Foto/Foto_M_Pycaret.JPG", use_column_width = True,)

if __name__ == "__introduccion__":
    introduccion()