#importamos las librErias necesarias.

import streamlit as st
import pandas as pd
import matplotlib as plt

#Cargamos los DataFrames necesarios para el proyecto.

df_demanda_nacional = pd.read_csv('demanda_nacional.csv')
df_demanda_comunidades = pd.read_csv('demanda_comunidades.csv')
df_Emisionas_diarias = pd.read_csv('EmisionesDiarias.csv')
df_Gener_dia_ren_no_ren= pd.read_csv('EmisionesDiarias.csv')
df_intercambio= pd.read_csv('intercambio.csv')
df_gen_dia_x_tecno= pd.read_csv('GeneracionDiariaXTecnologia.csv')

#Creamos el marco de trabajo de Streamlit.

def main():

    #Definimos un tÍtulo general para la página.
    st.header("MODELOS DE PREDICCIÓN DE SERIES TEMPORALES CON REDES NEURONALES")
    st.subheader("Usamos estos modelos para predecir diferentes variables del sistema electrico español")
    
    #Introcucimos imagenes principales para la página.
    st.image("PR3/Imgn_REE.JPG", width=500)
    st.image("PR3/Imgn_REE_2.JPG", width=300)

    #Creamos un MENÚ lateral para selecionar las distintal paginas del proyecto.
    st.sidebar.header('Menú')
    opcion = st.sidebar.selectbox('Seleccione una opción', ['INTRODUCCIÓN', 'MODELO DEMANDA', 'MODELO GENERACIÓN','MODELO EMISIONES'])
    
    #################################### INTRODUCCÓN ################################################
    #################################################################################################
    #################################################################################################

    if opcion == 'INTRODUCCIÓN':
        st.title('INTRODUCCIÓN')
        st.write('El objeto del siguiente proyecto es usar los diversos datos obtenidos de la API de red n\
                eléctrica para predecir datos futuros usando redes neuronales. n\
                Los datos actuales de demanda, generación, precios e intercambio nos servirán para n\
                entrenar un modelo de redes neuronales que nos permitirá predecir estas variables en un n\
                rango de tiempo determinado. Para lograr esto usamos modelos de redes neuronales que n\
                funcionen bien con predicción de variables en series temporales, como las redes neuronales n\
                con recursividad. n\
                En esta presentación web de Streamlit podréis navegar en el menú y ver como se realiza n\
                cada modelo y los resultados obtenidos del mismo, como norma general obtendremos un n\
                gráfico de predicción y unos valores de precisión del modelo que nos dirán cuán bueno es el n\
                mismo.')
        
    #################################### MODELO DEMANDA ############################################
    ################################################################################################
    ################################################################################################
    #Titulo
    elif opcion == 'MODELO DEMANDA':
        st.title('MODELO DEMANDA')

        #DataFrames
        with st.expander('Dataframes de Demanda', False):
            st.dataframe(df_demanda_nacional)
            st.dataframe(df_demanda_comunidades)

        #Texto
        st.write('Texto modelo demanda, mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm n\
                 mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm n\
                 mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')

    #################################### GENERACIÓN ################################################
    ################################################################################################
    ################################################################################################
    #Titulo
    elif opcion == 'MODELO GENERACIÓN':
        st.title('MODELO GENERACIÓN')
        #DataFrame
        with st.expander('Dataframe de Genración Nacional', False):
            st.dataframe(df_Gener_dia_ren_no_ren)
            st.dataframe(df_gen_dia_x_tecno)
        #Texto
        st.write('Texto modelo generación mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm n\
                 mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm n\
                 mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')

    ##################################### EMISIONES ################################################
    ################################################################################################
    ################################################################################################
    #Titulo
    elif opcion == 'MODELO EMISIONES':
        st.title('MODELO EMISIONES')
        #DataFrame
        with st.expander('Dataframe Emisiones', False):
            st.dataframe(df_Emisionas_diarias)
            
        #Texto
        st.write('Texto modelo Emisiones mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm n\
                 mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm n\
                 mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')   

        
    ############################# CARGAMOS IMÁGENES Y PIE  DE PÁGINA #######################
    ###############################################################################################
    ###############################################################################################    

    #tamaño_deseado_im_HaB = (300, 200) 
    st.image("PR3/Imgn_HaB.JPG", width=80)
    st.text('Autores del trabajo: Aitor, Eva, Adrian y Daniel Lema           Tutor: Daniel Tummler')
    

    ############################# CERRAMOS ESTRUCTURA DEL MODELO ########################
    ############################################################################################
    ############################################################################################

if __name__ == "__main__":
    main()