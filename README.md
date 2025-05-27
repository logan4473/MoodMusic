🎧 MoodMusic

MoodMusic is a fun Streamlit app that lets you explore Spotify playlists based on your mood.  
Select how you feel, and vibe instantly with embedded Spotify players — no login required (but it helps)!

---

🌟 Features

- 🎯 Mood selection: Happy, Sad, Chill, Energetic
- 🔎 Auto-fetches mood-matching Spotify playlists
- 🎵 Embedded Spotify players for instant listening
- 🔗 Clickable links to open playlists in Spotify
- 🔐 Secure Spotify API integration with Streamlit secrets

---

🚀 How to Run

1. Clone this repository
   git clone https://github.com/yourusername/MoodMusic.git
   cd MoodMusic

2. Install dependencies
   pip install -r requirements.txt

3. Set up Spotify API credentials

   - Go to Spotify Developer Dashboard
   - Create an app and get your Client ID and Client Secret

   Create a file at .streamlit/secrets.toml with:

   SPOTIPY_CLIENT_ID = "your-client-id"
   SPOTIPY_CLIENT_SECRET = "your-client-secret"

4. Run the app
   streamlit run main.py

---

📁 Project Structure

MoodMusic/
├── .streamlit/
│ └── secrets.toml # Your Spotify API keys
├── main.py # Streamlit app entry point
├── README.md # You're reading it
├── requirements.txt # Python dependencies

---

🛠 Requirements

- Python 3.7+
- Streamlit
- Spotipy

Create requirements.txt with:

streamlit
spotipy

---

📸 Screenshots

> Add screenshots here showing the app UI and Spotify player widgets.

---

🙌 Credits

Built by Girdhar — just for fun ✌️  
Using: Streamlit & Spotify Web API

---

📄 License

MIT License
