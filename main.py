import streamlit as st
import random
import os

st.set_page_config(page_title="MoodMusic", page_icon="🎧", layout="centered")

st.title("🎧 MoodMusic")
st.subheader("Select your mood and vibe with music!")

# Define mood-song mapping
mood_songs = {
    "😊 Happy": ["assets/happy1.mp3", "assets/happy2.mp3"],
    "😔 Sad": ["assets/sad1.mp3"],
    "🧘 Chill": ["assets/chill1.mp3", "assets/chill2.mp3"],
    "⚡ Energetic": ["assets/energetic1.mp3"]
}

# Display buttons for each mood
for mood in mood_songs:
    if st.button(mood):
        song = random.choice(mood_songs[mood])
        st.audio(song, format='audio/mp3')
        st.success(f"Playing a {mood} tune 🎵")

st.markdown("---")
st.caption("Built by Girdhar, just for fun ✌️")
