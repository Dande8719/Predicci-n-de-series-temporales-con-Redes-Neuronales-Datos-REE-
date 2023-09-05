import streamlit as st

def Autores():
    st.title('AUTORES:') 
        
        #Establecemos columnas para dar orden a los autores.
    col1, col2 = st.columns([1, 1])
    col3, col4,col5,col6 = st.columns([1, 1, 1, 1])
    col7, col8 = st.columns([1, 1])
    col9, col10,col11,col12 = st.columns([1, 1, 1, 1]) 
        #Autores:
    col1.subheader('EVA IGLESIAS') 
    col1.image('Foto/Eva_Iglesias_foto.jpg',width=150)   
    col3.markdown("[![Linkedin](<https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg>)](<https://www.linkedin.com/in/eva-iglesias-vieito-ingeniera-quimica/>)")   
    col4.markdown("[![GuitHub](<https://img.icons8.com/material-outlined/48/000000/github.png>)](<https://github.com/EvaIglesias17>)")

    col2.subheader('AITOR GONZALEZ') 
    col2.image('Foto/Aitor_Gonzalez_Foto.jpg',width=150)   
    col5.markdown("[![Linkedin](<https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg>)](<https://www.linkedin.com/in/adri%C3%A1n-ch%C3%A1vez-rodr%C3%ADguez/>)")   
    col6.markdown("[![GuitHub](<https://img.icons8.com/material-outlined/48/000000/github.png>)](<https://github.com/Rascasse80>)")

    col7.subheader('ADRIÁN CHÁVEZ RODRÍGEZ') 
    col7.image('Foto/Foto_Adrián_Chavez.jpg',width=150)   
    col9.markdown("[![Linkedin](<https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg>)](<https://www.linkedin.com/in/adri%C3%A1n-ch%C3%A1vez-rodr%C3%ADguez/>)")   
    col10.markdown("[![GuitHub](<https://img.icons8.com/material-outlined/48/000000/github.png>)](<https://github.com/adrianchz2001>)")


    col8.subheader('DANIEL LEMA') 
    col8.image('Foto/Foto_Linkedin_Daniel_Lema_2.jpeg',width=150)
    col11.markdown("[![Linkedin](<https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg>)](<https://www.linkedin.com/in/jose-daniel-lema-martinez/>)")   
    col12.markdown("[![GuitHub](<https://img.icons8.com/material-outlined/48/000000/github.png>)](<https://github.com/Dande8719?tab=followers>)")
    
   

if __name__ == "__Autores__":
    Autores()