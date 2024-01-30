from openai import OpenAI
import streamlit as st
import pandas as pd
import random
import math
from dotenv import load_dotenv
import os
import requests
from PIL import Image
from io import BytesIO

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load CSV files
races_data = pd.read_csv('races.csv')
classes_data = pd.read_csv('classes.csv')
alignments_data = pd.read_csv('alignments.csv')
backgrounds_data = pd.read_csv('backgrounds.csv')
appearances_data = pd.read_csv('appearances.csv',on_bad_lines='skip', encoding='utf-8')
flaws_data = pd.read_csv('flaws.csv',on_bad_lines='skip')


def get_image_url(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.images.generate(
    model="dall-e-2",
    prompt=prompt,
    size="256x256",
    quality="standard",
    n=1,
    )

    return response.data[0].url


def telecharger_et_sauvegarder_image(url, nom_fichier="image_telechargee.png"):
    try:
        # Récupérer le contenu de l'URL
        reponse = requests.get(url)
        reponse.raise_for_status()  # Vérifier s'il y a des erreurs lors de la récupération

        # Ouvrir l'image depuis le contenu binaire
        image = Image.open(BytesIO(reponse.content))

        # Sauvegarder l'image en tant que fichier PNG
        image.save(nom_fichier, format="PNG")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")




# Create Streamlit app
st.title("Random Character Generator")

def generate_random_character():
    # Randomly select character attributes
    random_race = random.choice(races_data['Race'])
    random_class = random.choice(classes_data['Class'])
    random_alignment = random.choice(alignments_data['Alignment'])
    random_background = random.choice(backgrounds_data['Background'])
    random_appearance = random.choice(appearances_data['Appearance'])
    random_flaws = random.sample(list(flaws_data['Flaw']), random.randint(1, 5))
    random_age = random.randrange(16, 66)
    flaws_string = ", ".join(random_flaws)

    character_data = {
        'Race': random_race,
        'Class': random_class,
        'Alignment': random_alignment,
        'Background': random_background,
        'Appearance': random_appearance,
        'Flaws': flaws_string,
        'Age': str(random_age)
    }
    #print(character_data)
    image_url = get_image_url("a picture of a dnd character with parameters " + ' '.join(character_data.values()) + ")")
    telecharger_et_sauvegarder_image(image_url)
    st.image("image_telechargee.png")
    # Display random character attributes
    st.write(f"**Race:** {random_race}")
    st.write(f"**Class:** {random_class}")
    st.write(f"**Age:** {random_age}")
    st.write(f"**Alignment:** {random_alignment}")
    st.write(f"**Background:** {random_background}")
    st.write(f"**Appearance:** {random_appearance}")
    st.write(f"**Flaws:** {', '.join(random_flaws)}")

# Display random character attributes
#generate_random_character()

# Add a "Reroll" button
if st.button("generate random DnD character"):
    st.empty()  # Clear the previous character attributes
    generate_random_character()
