#importamos las librErias necesarias.

import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px
import folium 
from urllib.request import urlopen
import json
from streamlit_folium import st_folium

#Cargamos los DataFrames necesarios para el proyecto.

df_demanda_nacional = pd.read_csv('demanda_nacional.csv')
df_demanda_comunidades = pd.read_csv('demanda_comunidades.csv')
df_Emisionas_diarias = pd.read_csv('EmisionesDiarias.csv')
df_Gener_dia_ren_no_ren= pd.read_csv('GeneracionDiariaRenNoRen.csv')
df_intercambio= pd.read_csv('intercambio.csv')
df_gen_dia_x_tecno= pd.read_csv('GeneracionDiariaXTecnologia.csv')

#Creamos el marco de trabajo de Streamlit.

def main():

    #Definimos un tÍtulo general para la página.
    st.header("MODELOS DE PREDICCIÓN DE SERIES TEMPORALES CON REDES NEURONALES")
    st.markdown(body = '<div style="text-align: justify; font-size: 20px; color:Gray;">Usamos estos modelos para predecir diferentes variables del sistema electrico español</div>',
                unsafe_allow_html = True)
    #st.markdown("#### Usamos estos modelos para predecir diferentes variables del sistema electrico español")
    col1, col2, col3 = st.columns([1, 6, 1])
    col4, col5, col6 = st.columns([2, 4, 2])
    #Introcucimos imagenes principales para la página.
    col2.image("Imgn_REE.JPG", use_column_width = True,)
    col5.image("Imgn_REE_2.JPG", use_column_width = True)

    #Creamos un MENÚ lateral para selecionar las distintal paginas del proyecto.
    st.sidebar.header('Menú')
    opcion = st.sidebar.selectbox('Seleccione una opción', ['INTRODUCCIÓN', 'MODELO DEMANDA', 'MODELO GENERACIÓN','MODELO EMISIONES'])
    
    #################################### INTRODUCCÓN ################################################
    #################################################################################################
    #################################################################################################

    if opcion == 'INTRODUCCIÓN':
        st.title('INTRODUCCIÓN')
        st.write('<div style="text-align: justify;">El objeto del siguiente proyecto es usar los diversos datos obtenidos de la API de red n\
                eléctrica para predecir datos futuros usando redes neuronales. n\
                Los datos actuales de demanda, generación, precios e intercambio nos servirán para n\
                entrenar un modelo de redes neuronales que nos permitirá predecir estas variables en un n\
                rango de tiempo determinado. Para lograr esto usamos modelos de redes neuronales que n\
                funcionen bien con predicción de variables en series temporales, como las redes neuronales n\
                con recursividad. n\
                En esta presentación web de Streamlit podréis navegar en el menú y ver como se realiza n\
                cada modelo y los resultados obtenidos del mismo, como norma general obtendremos un n\
                gráfico de predicción y unos valores de precisión del modelo que nos dirán cuán bueno es el n\
                mismo.</div>', unsafe_allow_html=True)
        
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

        # Texto
        st.write('Obtenemos los datos de demanda eléctrica nacional de la API de Red eléctrica de España, los n\
                 pasamos a GW/h y obtenemos una serie temporal de datos de 11 años de energía eléctrica n\
                 consumida en España, valores diarios.')
        
        # Imprimimos un grafico linal con plotly exprexx de demanda Nacional
        fig1 = px.line(df_demanda_nacional, 
                       x="Fecha", 
                       y="Energia Consumida Mw/h", 
                       title="Demanda Eléctrica Nacional")
        st.plotly_chart(figure_or_data = fig1, use_container_width = True)
        
        # Comentamos texto para demanda por comunidades 
        st.write('También obtenemos los datos de demanda de energía por comunidades autónomas.')

        #Preparamos los dataframes para usar folium en streamlit.
        df_medias = df_demanda_comunidades.drop('Fecha',axis=1)
        media = df_medias.mean()
        df_com = pd.DataFrame(media).reset_index()
        df_com.columns = ["Comunidades", "media"]
       

        # Imprimimos un grafico con folium para la demanda por comunidades.
        def create_choropleth_map():
            with urlopen("https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/spain-communities.geojson") as response:
                comunidades=json.load(response)
            # Tu código de creación de Choropleth map
            spain_map = folium.Map(location=[40.4637, -3.7492], zoom_start=6)
            folium.Choropleth(
                geo_data=comunidades,
                legend_name="Demanda media de energía 2012-2022",
                fill_color="OrRd",
                data=df_com,
                columns=["Comunidades", "media"],
                key_on="feature.properties.name"
            ).add_to(spain_map)
            return spain_map
        
        map = create_choropleth_map()
        st_folium(map)

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
    st.markdown("***")
    st.image("Imgn_HaB.JPG", width=80)
    st.text('Autores del trabajo: Aitor, Eva, Adrian y Daniel Lema           Tutor: Daniel Tummler')
    
    
    ############################# CERRAMOS ESTRUCTURA DEL MODELO ########################
    ############################################################################################
    ############################################################################################

if __name__ == "__main__":
    main()