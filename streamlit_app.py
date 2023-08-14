import streamlit as st
import pandas as pd
import random
import math

# Load CSV files
races_data = pd.read_csv('races.csv')
classes_data = pd.read_csv('classes.csv')
alignments_data = pd.read_csv('alignments.csv')
backgrounds_data = pd.read_csv('backgrounds.csv')
appearances_data = pd.read_csv('appearances.csv')
flaws_data = pd.read_csv('flaws.csv')


# Create Streamlit app
st.title("Random Character Generator")

# Randomly select character attributes
random_race = random.choice(races_data['Race'])
random_class = random.choice(classes_data['Class'])
random_alignment = random.choice(alignments_data['Alignment'])
random_background = random.choice(backgrounds_data['Background'])
random_appearance = random.choice(appearances_data['Appearance'])
#random_flaw = random.choice(flaws_data['Flaw'])
random_flaws = random.sample(list(flaws_data['Flaw']), random.randint(1, 5))


# Display random character attributes
st.write(f"**Race:** {random_race}")
st.write(f"**Class:** {random_class}")
st.write(f"**Alignment:** {random_alignment}")
st.write(f"**Background:** {random_background}")
st.write(f"**Appearance:** {random_appearance}")
st.write(f"**Flaws:** {random_flaws}")

