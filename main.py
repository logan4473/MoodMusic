import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Page setup
st.set_page_config(page_title="MoodMusic", page_icon="🎧", layout="centered")
st.title("🎧 MoodMusic")
st.subheader("Pick a mood and vibe with curated Spotify playlists!")

# Spotify credentials from Streamlit secrets
client_id = st.secrets["SPOTIPY_CLIENT_ID"]
client_secret = st.secrets["SPOTIPY_CLIENT_SECRET"]

# Set up Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))

# Mood choices
moods = ["😊 Happy", "😔 Sad", "🧘 Chill", "⚡ Energetic"]
selected_mood = st.selectbox("Choose a mood", moods)

# When user clicks
if st.button("Show Playlists"):
    search_term = selected_mood.split(" ", 1)[1] + " mood"
    results = sp.search(q=search_term, type="playlist", limit=5)

    playlists = results["playlists"]["items"]
    if not playlists:
        st.warning("No playlists found for this mood.")
    else:
        playlists = [playlist for playlist in playlists if playlist]
        for playlist in playlists:
            name = playlist["name"]
            playlist_id = playlist["uri"].split(":")[-1]
            playlist_url = playlist["external_urls"]["spotify"]

            # Embed Spotify player
            embed_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"
            st.markdown(
                f"""
                <iframe src="{embed_url}" width="100%" height="160" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
                """,
                unsafe_allow_html=True,
            )

            # Clickable name below player
            st.markdown(f"🔗 [**{name}**]({playlist_url})")
            st.markdown("---")

st.caption("Built by Girdhar, just for fun ✌️")
