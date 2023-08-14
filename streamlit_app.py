import streamlit as st
import pandas as pd
import random

# Load CSV files
#traits_data = pd.read_csv('personality_traits.csv')
classes_data = pd.read_csv('classes.csv')
alignments_data = pd.read_csv('alignments.csv')
backgrounds_data = pd.read_csv('backgrounds.csv')

# Create Streamlit app
st.title("Random Character Generator")

# Randomly select character attributes
#random_trait = random.choice(traits_data['Trait'])
random_class = random.choice(classes_data['Class'])
random_alignment = random.choice(alignments_data['Alignment'])
random_background = random.choice(backgrounds_data['Background'])

# Display random character attributes
#st.write(f"**Personality Trait:** {random_trait}")
st.write(f"**Class:** {random_class}")
st.write(f"**Alignment:** {random_alignment}")
st.write(f"**Background:** {random_background}")
