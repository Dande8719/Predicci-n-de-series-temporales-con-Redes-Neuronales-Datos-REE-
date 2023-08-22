#importamos las librErias necesarias.

import streamlit as st
import pandas as pd
import matplotlib as plt
import plotly.express as px
import folium 
from urllib.request import urlopen
import json
from streamlit_folium import st_folium
import seaborn as sns

#Cargamos los DataFrames necesarios para el proyecto.
df_precios = pd.read_csv("Precios por mes.csv")
df_demanda_nacional = pd.read_csv('demanda_nacional.csv')
df_demanda_comunidades = pd.read_csv('demanda_comunidades.csv')
df_Emisiones_diarias = pd.read_csv('EmisionesDiarias.csv')
df_Gener_dia_ren_no_ren= pd.read_csv('GeneracionDiariaRenNoRen.csv')
df_intercambio= pd.read_csv('intercambio.csv')
df_gen_dia_x_tecno= pd.read_csv('GeneracionDiariaXTecnologia.csv')

#Creamos el marco de trabajo de Streamlit.

def main():

    #Definimos un tÍtulo general para la página.
    st.header("MODELOS DE PREDICCIÓN DE SERIES TEMPORALES CON REDES NEURONALES")
    # st.markdown(body = '<div style="text-align: justify; font-size: 15px; color:Gray;">Usamos estos modelos para predecir diferentes variables del sistema electrico español</div>',
    #             unsafe_allow_html = True)
    st.markdown("##### Usamos distintos modelos para predecir diferentes variables del sistema electrico español")
    col1, col2, col3 = st.columns([2, 2, 2])
    col4, col5, col6 = st.columns([3, 1, 3])
    #Introcucimos imagenes principales para la página.
    col2.image("Imgn_REE.JPG", use_column_width = True,)
    col5.image("Imgn_REE_2.JPG", use_column_width = True)

    #Creamos un MENÚ lateral para selecionar las distintal paginas del proyecto.
    st.sidebar.header('Menú')
    opcion = st.sidebar.selectbox('Seleccione una opción', ['EDA(Exploratory Data Analisys)', 'MODELOS DE PREDICCIÓN', 'RESULTADOS Y CONCLUSIONES'])
    
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
        
    #################################### EDA (Exploratory Data Analisys) ###########################
    ################################################################################################
    ################################################################################################

    #Título

    elif opcion == 'EDA(Exploratory Data Analisys)':
        st.title('EDA(Exploratory Data Analisys)')

        # Texto Sobre los distintos análisis exploratorios de los datos.
        st.write('A continuación pueden escoger entre los distintos analisis exploratorios de datos n\
                 empezando por la generación de energía a nivel nacional, emisiones, demanda y acabando n\
                 por el intercambio de energía.')

        #st.selectbox.header('Menú Modelos')
        opcion = st.selectbox('Seleccione una opción', ['GENERACIÓN', 'EMISIONES', 'DEMANDA','PRECIOS'])


        if opcion == 'GENERACIÓN':
            st.title('EDA GENERACIÓN')

            st.write('Mientras que la generación de energías renovables muestra una tendencia creciente con el n\
                      tiempo, además de una serie temporal estacionalizada, la generación de energías no n\
                      renovables muestra una tendencia mínimamente decreciente, apuntando a ser casi n\
                      constante en el tiempo, y siendo también una serie temporal estacionalizada, algo a tomar n\
                      en cuenta a la hora de realizar predicciones.')  
            #Figura 1
            fig1=px.line(data_frame = df_Gener_dia_ren_no_ren,
                y = 'Generación Renovables GWh',
                x = 'Fechas',
                title = 'Evolución de la generación de energías renovables con el tiempo')
            st.plotly_chart(fig1)

            #Figura 2
            fig2= px.line(data_frame = df_Gener_dia_ren_no_ren,
             y = 'Generación No renovables GWh',
             x = 'Fechas',
             title = 'Evolución de la generación de energías NO renovables con el tiempo')
            st.plotly_chart(fig2)

            #Figura 3
            fig3=sns.barplot(data = df_demanda_comunidades)
            #fig3=plt.gcf().autofmt_xdate()
            st.pyplot(fig3)

            # if st.button("Modelo Pycam", key="Pycam"):
            #     st.write("Usamos el Modelo Pycam para predecir seri")

            # if st.button("Botón 2", key="button2"):
            #     st.write("¡Has hecho clic en el Botón 2!")
        if opcion == 'EMISIONES':
            st.title('EDA EMISIONES')

            st.write('Observamos como las emisiones de CO2 descienden sobre todo a partir del año 2019 \
                 produciendose una gran reducción de emisiones entre el año 2019 y el 2021 y habiendo un pequeño repunte \
                 debido a la gerra de Ukrania y las repercusiones de esta sobra el mercado energético.')

            fig4=px.line(data_frame = df_Emisiones_diarias,
             y = 'tCO2 eq./MWh',
             x = 'Fechas',
             title = 'Toneladas de CO2 emitidas por megavatio hora consumido (Tendencia a lo largo del tiempo)')
            st.plotly_chart(fig4)

        if opcion == 'DEMANDA':
            st.title('EDA DEMANDA')

            st.write('Obtenemos los datos de demanda eléctrica nacional de la API de Red eléctrica de España, los \
                 pasamos a GW/h y obtenemos una serie temporal de datos de 11 años de energía eléctrica \
                 consumida en España, valores diarios.')


            fig4 = px.line(data_frame = df_demanda_nacional, x = "Fecha", y = "Energia Consumida Mw/h")
            st.plotly_chart(fig4)

            
        if opcion == 'PRECIOS':
            st.title('EDA PRECIOS')

            st.write('Observamos que, debido a los valores anomarlmente elevados que se dieron durante \
                    los años 2022 y parte de 2021 y 2023, la distribución de los datos se ve notablemente \
                    afectada y representa un problema conocido en estadística como "cola pesada", que se \
                    da cuando valores de baja densidad (muy rara frecuencia) no son exponencialmente raros. \
                     Esto puede afectar negativamente a los modelos y, especialmente, a la estandarización de \
                    los datos, pues altera enormemente la media y la desviación típica.')
            
            
            
            fig7 = px.line(df_precios, x = 'Meses', y = '€/Mwh', title="Precios en €/Mwh") # Graficamos la serie temporal de precios
            st.plotly_chart(fig7)

            # sns.set(style="whitegrid")
            # plt.figure(figsize=(8, 6))
            # fig2=sns.histplot(df_precios['€/Mwh'], kde = True)
            # st.pyplot(fig3)


    #################################### MODELOS DE PREDICCIÓN #####################################
    ################################################################################################
    ################################################################################################
    
    #Titulo
    elif opcion == 'MODELOS DE PREDICCIÓN':
        st.title('MODELOS DE PREDICCIÓN')
        #Texto
        st.write('A Continuación seleccionamos entre las distintas variables a predecir para ver los resultados  n\
                  de los modelos que usamos para la predicción de las mismas.')

        opcion = st.selectbox('Seleccione una opción', ['GENERACIÓN X TEC', 'GENERACIÓN REN', 'EMISIONES','DEMANDA','DEMANDA X COMUNIDAD'])

        #Opcione de predicción por generación 
        if opcion == 'GENERACIÓN X TEC':
            st.title('MODELO GENERACIÓN X TEC')

            st.write('Obtenemos los datos de demanda eléctrica nacional de la API de Red eléctrica de España, los n\
                 pasamos a GW/h y obtenemos una serie temporal de datos de 11 años de energía eléctrica n\
                 consumida en España, valores diarios.') 
            
            #Creamos una serie de botones para seleccionar el tipo de modelo a aplicar.
            if st.button("Modelo Pycam", key="Pycam"):
                 st.write("Usamos el Modelo Pycam para predecir series temporales .......")

            if st.button("Modelo Prophet", key="Modelo prophet"):
                 st.write("¡Has hecho clic en el Modelo Prophet!")

            if st.button("Modelo X", key="Modelo X"):
                 st.write("¡Has hecho clic en el Modelo X")
        
        if opcion == 'GENERACIÓN REN':
            st.title('MODELO GENERACIÓN REN')

            st.write('Obtenemos los datos de demanda eléctrica nacional de la API de Red eléctrica de España, los n\
                 pasamos a GW/h y obtenemos una serie temporal de datos de 11 años de energía eléctrica n\
                 consumida en España, valores diarios.')

        if opcion == 'EMISIONES':
            st.title('MODELO EMISIONES')

            st.write('Obtenemos los datos de demanda eléctrica nacional de la API de Red eléctrica de España, los n\
                 pasamos a GW/h y obtenemos una serie temporal de datos de 11 años de energía eléctrica n\
                 consumida en España, valores diarios.')
            
        if opcion == 'DEMANDA':
            st.title('MODELO DEMANDA')

            st.write('Obtenemos los datos de demanda eléctrica nacional de la API de Red eléctrica de España, los n\
                 pasamos a GW/h y obtenemos una serie temporal de datos de 11 años de energía eléctrica n\
                 consumida en España, valores diarios.')
        
        if opcion == 'DEMANDA X COMUNIDAD':
            st.title('MODELO DEMANDA X COMUNIDAD')

            st.write('Obtenemos los datos de demanda eléctrica nacional de la API de Red eléctrica de España, los n\
                 pasamos a GW/h y obtenemos una serie temporal de datos de 11 años de energía eléctrica n\
                 consumida en España, valores diarios.')

    ##################################### RESULTADOS Y CONCLUSIONES ################################
    ################################################################################################
    ################################################################################################
    #Titulo
    elif opcion == 'RESULTADOS Y CONCLUSIONES':
        st.title('RESULTADOS Y CONCLUSIONES')
        
            
        #Texto
        st.write('Los datos de emisiones de CO2 al igual que la generación son datos diarios obtenidos a nivel n\
                  nacional y divididos por tecnologías. En este grafico podemos interaccionar con las emisiones n\
                 de las diferentes tecnologías.') 

        
        

        

    ############################# CARGAMOS IMÁGENES Y PIE  DE PÁGINA #######################
    ###############################################################################################
    ###############################################################################################    

    #tamaño_deseado_im_HaB = (300, 200) 
    st.markdown("***")
    st.image("Imgn_HaB.JPG", width=80)
    st.text('Autores del trabajo: Aitor, Eva, Adrian y Daniel Lema          Tutor: Daniel Tummler ')
    
    
    ############################# CERRAMOS ESTRUCTURA DEL MODELO ########################
    ############################################################################################
    ############################################################################################

if __name__ == "__main__":
    main()