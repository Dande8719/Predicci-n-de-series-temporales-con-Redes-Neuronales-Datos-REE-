#Importamos las librerias necesarias.
import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px
import imageio
from streamlit_lottie import st_lottie
import requests
from streamlit_option_menu import option_menu

#Importamos funciones de codigo en otros archivos
from introduccion import introduccion
from eda import eda
from Modelos import Modelos
from Autores import Autores


#from pycaret.time_series import TSForecastingExperiment 
# Cargamos los DataFrames necesarios para el proyecto. Tengo todos los del EDA.

df_precios = pd.read_csv("DF\Precios por mes.csv")
df_demanda_nacional = pd.read_csv('DF\demanda_nacional.csv')
df_demanda_comunidades = pd.read_csv('DF\demanda_comunidades.csv')
df_Emisiones_diarias = pd.read_csv('DF\EmisionesDiarias.csv')
df_Gener_dia_ren_no_ren= pd.read_csv('DF\GeneracionDiariaRenNoRen.csv')
df_intercambio= pd.read_csv('DF\intercambio.csv')
df_gen_dia_x_tecno= pd.read_csv('DF\GeneracionDiariaXTecnologia.csv')
df_ipc = pd.read_excel("DF\IPC energía - Eurostat.xlsx", sheet_name = "Sheet 2")

#Creamos el marco de trabajo de Streamlit.

def main():

    st.set_page_config(
    page_title="MODELOS REE",
    page_icon="⚡️",
    )

    # Definimos un tÍtulo general para la página.
    st.header("MODELOS DE PREDICCIÓN DE SERIES TEMPORALES")
    # st.markdown(body = '<div style="text-align: justify; font-size: 15px; color:Gray;">Usamos estos modelos para predecir diferentes variables del sistema electrico español</div>',
    #             unsafe_allow_html = True)
    st.markdown("##### Usamos distintos modelos para predecir diferentes variables del sistema electrico español")

    

    
    #Creamos un MENÚ.
    opcion=st.sidebar.selectbox("Menú", 
                                ["INTRODUCCIÓN",
                                 "ANALISIS EXPLORATORIO DE LOS DATOS",
                                 "MODELOS DE PREDICCIÓN",
                                 "RESULTADOS Y CONCLUSIONES",
                                 "AUTORES"])
   
         

    
    #################################### INTRODUCCÓN ################################################
    #################################################################################################
    #################################################################################################

    if opcion == 'INTRODUCCIÓN':
        introduccion()

    #################################### EDA (Exploratory Data Analisys) ###########################
    ################################################################################################
    ################################################################################################

    #Título

    elif opcion == 'ANALISIS EXPLORATORIO DE LOS DATOS':
        
        eda(df_Gener_dia_ren_no_ren = df_Gener_dia_ren_no_ren.copy(),
            df_Emisiones_diarias    = df_Emisiones_diarias.copy(),
            df_demanda_nacional     = df_demanda_nacional.copy(),
            df_demanda_comunidades  = df_demanda_comunidades.copy(),
            df_precios              = df_precios.copy())


    #################################### MODELOS DE PREDICCIÓN #####################################
    ################################################################################################
    ################################################################################################
    
    #Titulo
    elif opcion == 'MODELOS DE PREDICCIÓN':
        Modelos()

    ##################################### RESULTADOS Y CONCLUSIONES ################################
    ################################################################################################
    ################################################################################################
    #Titulo
    elif opcion == 'RESULTADOS Y CONCLUSIONES':
        st.title('RESULTADOS Y CONCLUSIONES') 

        st_lottie(requests.get("https://lottie.host/7f675139-8c7f-4cd0-93c0-0d1831dcfdc6/Kb96HXJOD7.json").json(), height=250, key="model")
        #Texto
        st.write('Los datos de emisiones de CO2 al igual que la generación son datos diarios obtenidos a nivel n\
                  nacional y divididos por tecnologías. En este grafico podemos interaccionar con las emisiones n\
                 de las diferentes tecnologías.') 
        
       

    elif opcion == 'AUTORES':
        
        Autores()
    ############################# CARGAMOS IMÁGENES Y PIE  DE PÁGINA #######################
    ###############################################################################################
    ###############################################################################################    

    #tamaño_deseado_im_HaB = (300, 200) 
    st.markdown("***")
    
    col1, col2, col3 = st.columns([2, 3, 1])
    #Introcucimos imagenes principales para la página.
    col1.image("Foto/Imgn_HaB.JPG", width=80)
    col2.image("Foto/Imgn_REE.JPG", use_column_width = True,)
    col3.image("Foto/Imgn_REE_2.JPG", use_column_width = True)
    
    
    ############################# CERRAMOS ESTRUCTURA DEL MODELO ########################
    ############################################################################################
    ############################################################################################

if __name__ == "__main__":
    main()