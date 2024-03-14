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
        return pokemon['name'], pokemon['types'], pokemon['height'], pokemon['weight'], pokemon['moves'], pokemon['cries']['latest'], pokemon['id'], pokemon['stats']
    except:
        return 'Error', np.NAN, np.NAN, np.NAN, np.NAN, np.NAN

# choose a pokemon
st.subheader("Choose a Pokemon")   
pokemon_number = st.number_input("pick a pokemon",
                           min_value=1,
                           max_value=1025,
                           label_visibility="hidden"
                           )

name, types, height, weight, moves, cry, id, stats = get_details(pokemon_number)

height = height * 10
num_moves = len(moves)
move_lst = [moves[i]['move']['name'] for i in range(0, len(moves))]
moves_str = ', '.join(move_lst)

stats_tbl = pd.DataFrame(data = [], columns = ['Value'])

stats_tbl.loc['height'] = height
stats_tbl.loc['weight'] = weight
stats_tbl.loc['base hp'] = stats[0]['base_stat']
stats_tbl.loc['base attack'] = stats[1]['base_stat']
stats_tbl.loc['base defence'] = stats[2]['base_stat']
stats_tbl.loc['base special attack'] = stats[3]['base_stat']
stats_tbl.loc['base special defence'] = stats[4]['base_stat']
stats_tbl.loc['base speed'] = stats[5]['base_stat']

m_type = types[0]['type']['name']

img = f'https://github.com/PokeAPI/sprites/blob/master/sprites/pokemon/other/official-artwork/{id}.png?raw=true'
shiny_img = f'https://github.com/PokeAPI/sprites/blob/master/sprites/pokemon/other/official-artwork/shiny/{id}.png?raw=true'

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


height_data = pd.DataFrame({'Pokemon': ['Weedle', name, 'Eternatus'], 'Height': [30, height, 2000]})
weight_data = pd.DataFrame({'Pokemon': ['Gastly', name, 'Celesteela'], 'Weight': [1, weight, 9999]})

fig, (axs1, axs2) = plt.subplots(1, 2, figsize=(15, 8))
sns.barplot(data=height_data, x='Pokemon', y='Height', palette=colours, ax=axs1)
sns.barplot(data=weight_data, x='Pokemon', y='Weight', palette=colours, ax=axs2)

# disply pokemon details
st.subheader(f'Name: {name}')

colm1, colm2 = st.columns(2)
with colm1:
    on = st.toggle('Shiny', False)
    if on:
        st.image(shiny_img, width=350)
    else:
        st.image(img, width=350)
    
    for i in range(0, len(types)):
        st.subheader(f'{types[i]["type"]["name"]} type')

with colm2:
    st.audio(cry)
    st.table(stats_tbl)
    
with st.expander(f'Moves: {num_moves}'):
    st.write(moves_str)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Height VS largest and smallest pokemon")

with col2:
    st.subheader("Weight VS heaviest and lightest pokemon")
    
st.pyplot(fig.figure)
plt.close()

  

    
    

