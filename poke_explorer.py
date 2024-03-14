### IMPORT FUNCTIONS ###
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import requests

st.title("Pokemon Explorer")

@st.cache_data
def get_details(poke_number):
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
        response = requests.get(url)
        pokemon = response.json()
        return pokemon['name'], pokemon['types'][0]['type']['name'], pokemon['height'], pokemon['weight'], pokemon['moves'], pokemon['sprites']['front_default'], pokemon['cries']['latest']
    except:
        return 'Error', np.NAN, np.NAN, np.NAN, np.NAN, np.NAN

# choose a pokemon
st.subheader("Choose a Pokemon")   
pokemon_number = st.number_input("pick a pokemon",
                           min_value=1,
                           max_value=1025,
                           label_visibility="hidden"
                           )

name, m_type, height, weight, moves, img, cry = get_details(pokemon_number)
height = height * 10
num_moves = len(moves)
move_lst = [moves[i]['move']['name'] for i in range(0, len(moves))]
moves_str = ', '.join(move_lst)

height_data = pd.DataFrame({'Pokemon': ['Weedle', name, 'Onix'], 'Height': [30, height, 880]})

if m_type == 'grass':
   poke_colour = 'limegreen'
elif m_type == 'fire':
    poke_colour = 'red'
elif m_type == 'water':
    poke_colour = 'blue'
elif m_type == 'bug':
    poke_colour = 'darkgreen'
elif m_type == 'normal':
    poke_colour = 'gold'
elif m_type == 'poison':
    poke_colour = 'purple'
elif m_type == 'electric':
    poke_colour = 'yellow'
elif m_type == 'ground':
    poke_colour = 'brown'
elif m_type == 'fairy':
    poke_colour = 'pink'
elif m_type == 'fighting':
    poke_colour = 'saddlebrown'
elif m_type == 'psychic':
    poke_colour = 'violet'
elif m_type == 'rock':
    poke_colour = 'darkgoldenrod'
elif m_type == 'ghost':
    poke_colour = 'black'
elif m_type == 'ice':
    poke_colour = 'lightblue'
elif m_type == 'dragon':
    poke_colour = 'darkred'
elif m_type == 'dark':
    poke_colour = 'darkslateblue'
else:
    poke_colour = 'turquoise'
    

colours = ['grey', poke_colour, 'grey']

graph = sns.barplot(data=height_data, 
                    x='Pokemon', 
                    y='Height', 
                    palette=colours)

# disply pokemon details
st.subheader(f'Name: {name}')

colm1, colm2 = st.columns(2)
with colm1:
    st.image(img, width=150)
    st.audio(cry)
with colm2:
    st.write(f'Main type: {m_type}')
    st.write(f'Height: {height}')
    st.write(f'Weight: {weight}')
    with st.expander(f'Moves: {num_moves}'):
        st.write(moves_str)

st.subheader("Height compared to largest and smallest pokemon")
st.pyplot(graph.figure)
