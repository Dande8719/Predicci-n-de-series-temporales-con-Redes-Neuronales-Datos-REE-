import streamlit as st
import plotly.express as px

def eda(df_Gener_dia_ren_no_ren,
        df_Emisiones_diarias,
        df_demanda_nacional,
        df_demanda_comunidades,
        df_precios):
    
    st.title('ANALISIS EXPLORATORIO DE LOS DATOS')

    # Texto Sobre los distintos análisis exploratorios de los datos.
    st.write('A continuación pueden escoger entre los distintos analisis exploratorios de datos \
                empezando por la generación de energía a nivel nacional, emisiones, demanda y acabando \
                por el intercambio de energía.')

    #st.selectbox.header('Menú Modelos')
    opcion = st.selectbox('Seleccione una opción', ['GENERACIÓN', 'EMISIONES', 'DEMANDA','PRECIOS'])


    if opcion == 'GENERACIÓN':
        st.title('EDA GENERACIÓN')

        st.write('Mientras que la generación de energías renovables muestra una tendencia creciente con el \
                    tiempo además de una serie temporal estacionalizada, la generación de energías no \
                    renovables muestra una tendencia mínimamente decreciente, apuntando a ser casi \
                    constante en el tiempo y siendo también una serie temporal estacionalizada, algo a tomar \
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
        #fig3=sns.barplot(data = df_demanda_comunidades)
        #fig3=plt.gcf().autofmt_xdate()
        #st.pyplot(fig3)

        
    if opcion == 'EMISIONES':
        st.title('EDA EMISIONES')

        st.write('Observamos como las emisiones de CO2 descienden sobre todo a partir del año 2019 \
                produciendose una gran reducción de emisiones entre el año 2019 y el 2021 y habiendo un pequeño repunte \
                debido a la gerra de Ucrania y las repercusiones de esta sobra el mercado energético.')

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

        X1=dict(df_demanda_comunidades.sum()[2:]).values()
        #   st.write(X1)
        fig5= px.bar(x=df_demanda_comunidades.columns[2:], y=X1, title='Demanda electrica por comunidades')
        st.plotly_chart(fig5)
        
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

if __name__ == "__eda__":
    eda()