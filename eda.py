import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import pandas as pd

def eda(df_demanda_nacional,
        df_demanda_comunidades,
        df_precios,
        df_emis_plt,
        df_gen_plt_eda):
    
    st.title('ANALISIS EXPLORATORIO DE LOS DATOS')

    # Texto Sobre los distintos análisis exploratorios de los datos.
    st.write('A continuación pueden escoger entre los distintos analisis exploratorios de datos \
                empezando por la generación de energía a nivel nacional, emisiones, demanda y acabando \
                por los precios de la energía')
    # Animación lottie
    st_lottie(requests.get("https://lottie.host/c16d2351-863a-48a7-b143-735071d01f92/JQ2hcUD9HM.json").json(), height=250, key="model")

    # st.selectbox.header('Menú Modelos')
    opcion = st.selectbox('Seleccione una opción', ['GENERACIÓN', 'EMISIONES', 'DEMANDA','PRECIOS'])

    ################################################## GENERACIÓN ############################################################## 

    if opcion == 'GENERACIÓN':
        st.title('EDA GENERACIÓN')

        st.write('Mientras que la generación de energías renovables muestra una tendencia creciente con el \
                    tiempo además de una serie temporal estacionalizada, la generación de energías no \
                    renovables muestra una tendencia mínimamente decreciente, apuntando a ser casi \
                    constante en el tiempo y siendo también una serie temporal estacionalizada, algo a tomar \
                    en cuenta a la hora de realizar predicciones.') 
        
        # Preparamos los Filtros
        renovables = ['Hidráulica','Hidroeólica',
                        'Solar fotovoltaica',
                        'Solar térmica',
                        'Otras renovables',
                        'Eólica',]
        
        #Creamos los filtros para filtrar por año y por renovable o no renovable.
        with st.expander('Filtros'):
                selected = st.multiselect(label = 'Tipo de energía',
                    options = ['Renovables', 'No renovables'],
                    default = ['Renovables','No renovables'],
                    key = 'generación'
                    )
        
                from_ = st.slider('Desde', 2014, 2022, 2014, key = 'generación_from')
                to = st.slider('Hasta', from_, 2022, 2022, key = 'generación_to')

        columns_gen = [x for x in df_gen_plt_eda.columns if 'Generación' in x]

        empty = False

        if len(selected) == 2:
                columns = [x for x in columns_gen] + ['Años']
        elif len(selected) == 0:
                empty = True
        elif selected[0] == 'Renovables':
                columns = [x for x in columns_gen if x[11:-4] in renovables] + ['Años']
        elif selected[0] == 'No renovables':
                columns = [x for x in columns_gen if x[11:-4] not in renovables] + ['Años']

        if not empty:

                generacion = df_gen_plt_eda[columns]
                generacion = generacion[generacion['Años'].between(from_, to)]
                
                #Plot generación por tecnologias barras.
                fig=px.bar(data_frame = generacion,
                x          = "Años",
                y          = generacion.columns[:],
                title      ="Evolución de la generación energética por tecnología, Gráfico de barras")

                st.plotly_chart(figure_or_data = fig, use_container_width = True)
        
        
                #Plot generación por tecnologias Lineal.
                fig2=px.line(data_frame = generacion,
                        x = "Años",
                        y = generacion.columns[:],
                        title = "Evolución de la generación energética por tecnología")
                st.plotly_chart(fig2)


    ################################################## EMISIONES ##############################################################    
    
    if opcion == 'EMISIONES':
        st.title('EDA EMISIONES')

        st.write('Observamos como las emisiones de CO2 descienden sobre todo a partir del año 2019 \
                produciendose una gran reducción de emisiones entre el año 2019 y el 2021 y habiendo un pequeño repunte \
                debido a la gerra de Ucrania y las repercusiones de esta sobra el mercado energético.')

        fig3=px.bar(data_frame = df_emis_plt,
                    x          = "Años",
                    y          = df_emis_plt.columns[1:-2],
                    title = "Emisiones de CO2")
    
        st.plotly_chart(figure_or_data = fig3, use_container_width = True)


        fig4=px.line(data_frame = df_emis_plt,
                x = "Años",
                y = "tCO2 eq./MWh",
                title = "Relación entre emisiones de CO2 y energía generada")


        st.plotly_chart(figure_or_data = fig4, use_container_width = True)

    ################################################## DEMANDA ##############################################################
    if opcion == 'DEMANDA':
        st.title('EDA DEMANDA')
        df_demanda_nacional = df_demanda_nacional.drop(columns=["Unnamed: 0"])
        df_demanda_nacional["Fecha"]=df_demanda_nacional["Fecha"].apply(lambda x : x.split("-")[0])
        df_demanda_nacional["Fecha"]=df_demanda_nacional["Fecha"].apply(lambda x : int(x))
        df_demanda_nacional=df_demanda_nacional.groupby("Fecha")['Energia Consumida Mw/h'].sum()
        df_demanda_nacional=pd.DataFrame(df_demanda_nacional)


        st.write('Obtenemos los datos de demanda eléctrica nacional de la API de Red eléctrica de España, los \
                pasamos a GW/h y obtenemos una serie temporal de datos de 11 años de energía eléctrica \
                consumida en España, valores diarios.')
        from_ = st.slider('Desde', 2014, 2022, 2014, key = 'generación_from')
        to = st.slider('Hasta', from_, 2022, 2022, key = 'generación_to')

        generacion = df_demanda_nacional
        generacion = generacion.reset_index()
        generacion = generacion[generacion["Fecha"].between(from_, to)]

        fig5=px.bar(data_frame = generacion,
                x          = "Fecha",
                y          = generacion.columns[1:],
                title      ="")

        st.plotly_chart(figure_or_data = fig5, use_container_width = True)

        st.write('Observamos que la demanda eléctrica en las distintas comunidades está muy relacionada con la población, \
                las comunidades mas pobladas son las que mas energía demandan. (EJ: Andalucía, Cataluña y Madrid.) ')
        
        X1=dict(df_demanda_comunidades.sum()[2:]).values()    #¿¿¿Como ordeno esto???
        #   st.write(X1)
        fig6= px.bar(x=df_demanda_comunidades.columns[2:],
                      y=X1, 
                      title='Demanda electrica por comunidades')
        st.plotly_chart(fig6)

    ################################################## PRECIOS ##############################################################    
    if opcion == 'PRECIOS':
        st.title('EDA PRECIOS')

        st.write('Observamos que, debido a los valores anomarlmente elevados que se dieron durante \
                los años 2022 y parte de 2021 y 2023, la distribución de los datos se ve notablemente \
                afectada y representa un problema conocido en estadística como "cola pesada", que se \
                da cuando valores de baja densidad (muy rara frecuencia) no son exponencialmente raros. \
                    Esto puede afectar negativamente a los modelos y, especialmente, a la estandarización de \
                los datos, pues altera enormemente la media y la desviación típica.')
        
        # Graficamos la serie temporal de precios
        fig7 = px.line(df_precios, x = 'Meses',
                        y = '€/Mwh',
                          title="Precios en €/Mwh") 
        st.plotly_chart(fig7)

    

if __name__ == "__eda__":
    eda()