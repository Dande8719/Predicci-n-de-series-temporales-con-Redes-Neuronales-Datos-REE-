import streamlit as st

def Autores():
    st.title('AUTORES:') 
        

    col1, col2 = st.columns([1, 1])
    col3, col4 = st.columns([1, 1])  
        #Autores:
    col1.subheader('EVA IGLESIAS') 
    col1.image('Foto/Eva_Iglesias_foto.jpg',width=200)   
    col1.write('Linkedin:  ''https://www.linkedin.com/in/eva-iglesias-vieito-ingeniera-quimica/')
    col1.write('GuitHub:  ''https://github.com/EvaIglesias17')

    col2.subheader('AITOR GONZALEZ') 
    col2.image('Foto/Aitor_Gonzalez_Foto.jpg',width=200)   
    col2.write('Linkedin:  ''https://www.linkedin.com/in/aitorgonzalezp/')
    col2.write('GuitHub:  ''https://github.com/Rascasse80')

    col3.subheader('ADRIÁN CHÁVEZ RODRÍGEZ ') 
    col3.image('Foto/Foto_Adrián_Chavez.jpg',width=200)   
    col3.write('Linkedin:  ''https://www.linkedin.com/in/adri%C3%A1n-ch%C3%A1vez-rodr%C3%ADguez/')
    col3.write('GuitHub:  ''https://github.com/adrianchz2001')



    col4.subheader('DANIEL LEMA ') 
    col4.image('Foto/Foto_Linkedin_Daniel_Lema_2.jpeg',width=200)   
    col4.write('Linkedin:  ''https://www.linkedin.com/in/jose-daniel-lema-martinez/')
    col4.write('GuitHub:  ''https://github.com/Dande8719?tab=followers')

if __name__ == "__Autores__":
    Autores()