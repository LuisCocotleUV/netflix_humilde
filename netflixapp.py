import streamlit as st
import pandas as pd
import codecs

st.title("Netflix App")
st.header("Luis David Cocotle Yáñez")
st.header("S20006746")

DATA_URL = ('movies.csv')
sidebar= st.sidebar
st.sidebar.image("matricula.jpeg")
st.sidebar.markdown("##")

@st.cache_data
def load_data(nrows):
    f = codecs.open(DATA_URL,'r', encoding='latin')
    data=pd.read_csv(f,nrows=nrows)
    return data

def filtro_pelicula(pelicula):
    pelicula_filt = data[data['name'].str.upper().str.contains(pelicula)]
    return pelicula_filt

def filtro_director(director):
    director_filt = data[data['director'] == director]
    return director_filt

data_load_state= st.text("Loading data...")
data= load_data(1000)
data_load_state.text("Done!")

st.header("Peliculas")
agree=sidebar.checkbox("Mostrar todas las peliculas")
if agree:
    st.dataframe(data)

titulofilme = st.sidebar.text_input('Titulo de la pelicula :')
botonBuscar = st.sidebar.button('Buscar pelicula')

if (botonBuscar):
   peliculas = filtro_pelicula(titulofilme.upper())
   count_row = peliculas.shape[0]  # Gives number of rows
   st.write(f"Total de peliculas mostradas : {count_row}")
   st.write(peliculas)

selDirector = st.sidebar.selectbox("Director", data['director'].unique())
botonFiltroDirector = st.sidebar.button('Filtro director')

if (botonFiltroDirector):
   director = filtro_director(selDirector)
   count_row = director.shape[0]  # Gives number of rows
   st.write(f"Total de peliculas : {count_row}")

   st.dataframe(director)