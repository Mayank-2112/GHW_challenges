import requests
import streamlit as st
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

#main
st.title("Pokemon Dashboard")

res = requests.get('https://pokeapi.co/api/v2/pokemon?limit=12')
if res.status_code == 200:
    data = res.json()
    pokemon = data['results']
    
    for pok in pokemon:
        with st.container(border=True):
            st.write(pok['name'])
            sprite_url = pok['url']
            sprite_res = requests.get(sprite_url)
            if sprite_res.status_code == 200:
                sprite_data = sprite_res.json()
                sprite_front = sprite_data['sprites']['front_default']
                st.image(sprite_front, width=150)
            else:
                st.error("Failed to fetch sprite for {pokemon['name']}")

else:
    st.error('Failed to fetch pokemons from api')