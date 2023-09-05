#Importamos las librerias necesarias.
import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px
from streamlit_lottie import st_lottie  #Libreria necesaria para trabajar con lotties archivos json animados
import requests
from streamlit_option_menu import option_menu    #Libreria necesaria para trabajar con lotties archivos json animados

#Importamos funciones de codigo en otros archivos
from introduccion import introduccion
from eda import eda
from Modelos import Modelos
from Autores import Autores

# Cargamos los DataFrames necesarios para el proyecto. Tengo todos los del EDA.

#df = pd.read_csv('DF\DF_REE.csv')
df_precios = pd.read_csv("DF\Precios por mes.csv")
df_demanda_nacional = pd.read_csv('DF\demanda_nacional.csv')
df_demanda_comunidades = pd.read_csv('DF\demanda_comunidades.csv')
#df_Emisiones_diarias = pd.read_csv('DF\EmisionesDiarias.csv')
#df_Gener_dia_ren_no_ren= pd.read_csv('DF\GeneracionDiariaRenNoRen.csv')
df_intercambio= pd.read_csv('DF\intercambio.csv')
#df_gen_dia_x_tecno= pd.read_csv('DF\GeneracionDiariaXTecnologia.csv')
df_ipc = pd.read_excel("DF\IPC energía - Eurostat.xlsx", sheet_name = "Sheet 2")
df_emis_plt = pd.read_csv('DF\emis_plt_eda.csv')
df_gen_plt_eda = pd.read_csv('DF\gen_plt_eda.csv')
df_pred_dem= pd.read_csv('DF\Prediccion Demanda Nacional - 1 step.csv')
df_pred_prec=pd.read_csv('DF\Predicciones a futuro de precios (abril 2023 a agosto 2024).csv')



#Creamos el marco de trabajo de Streamlit.

def main():

    st.set_page_config(
    page_title="MODELOS REE",
    page_icon="⚡️",
    )

    # # Definimos un tÍtulo y subtítulo general para la página.
    # st.header("MODELOS DE PREDICCIÓN DE SERIES TEMPORALES")
    # st.markdown("##### Usamos distintos modelos para predecir diferentes variables del sistema electrico español")

    # Creamos un MENÚ.
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

    elif opcion == 'ANALISIS EXPLORATORIO DE LOS DATOS':
        
        eda(df_demanda_nacional     = df_demanda_nacional.copy(),
            df_demanda_comunidades  = df_demanda_comunidades.copy(),
            df_precios              = df_precios.copy(),
            df_emis_plt             = df_emis_plt.copy(),
            df_gen_plt_eda          = df_gen_plt_eda.copy()
            )

    #################################### MODELOS DE PREDICCIÓN #####################################
    ################################################################################################
    ################################################################################################
    
    elif opcion == 'MODELOS DE PREDICCIÓN':
        Modelos()

    ##################################### RESULTADOS Y CONCLUSIONES ################################
    ################################################################################################
    ################################################################################################
    
    elif opcion == 'RESULTADOS Y CONCLUSIONES':
        st.title('RESULTADOS Y CONCLUSIONES') 

        st_lottie(requests.get("https://lottie.host/7f675139-8c7f-4cd0-93c0-0d1831dcfdc6/Kb96HXJOD7.json").json(), height=250, key="model")
        # Texto
        st.write('<div style="text-align: justify;">  \
                                 \
                                </div>', unsafe_allow_html=True) 
        
        # Gráficas predicciones.
        # Demanda
        fig24=px.line(data_frame = df_pred_dem,
                    x = "Fechas",
                    y =  ["Predicciones"],  
                    title = "Predicción demanda energética nacional Redes Neuronales")    

        st.plotly_chart(figure_or_data = fig24, use_container_width = True)
        #Precios
        fig25=px.line(data_frame = df_pred_prec,
                    x = "Fecha",
                    y =  ["Predicciones"],  
                    title = "Predicción precios mercado eléctrico con Redes Neuronales")    

        st.plotly_chart(figure_or_data = fig25, use_container_width = True)


    elif opcion == 'AUTORES':  
        Autores()

    ############################# CARGAMOS IMÁGENES Y PIE  DE PÁGINA #######################
    ###############################################################################################
    ###############################################################################################    

    st.markdown("***")
    col1, col2, col3 = st.columns([2, 3, 1])
    #Introcucimos imagenes principales para la página.
    col1.image("Foto/Imgn_HaB.JPG", width=80)
    col2.image("Foto/Imgn_REE.JPG", width=260)
    col3.image("Foto/Imgn_REE_2.JPG", width=100)
    
    ############################# CERRAMOS ESTRUCTURA DEL MODELO ########################
    ############################################################################################
    ############################################################################################

if __name__ == "__main__":
    main()