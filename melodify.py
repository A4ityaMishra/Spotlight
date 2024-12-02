import streamlit as st
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from textblob import TextBlob
from secret1 import ID, SECRET
import random

client_id = ID
client_secret = SECRET
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Mood feature mapping, will use textblob for cases not included in this dict --> done by Rohan
mood_data = {
    "very happy": {"energy": 0.9, "valence": 0.9, "genre": "dance"},
    "happy": {"energy": 0.8, "valence": 0.8, "genre": "pop"},
    "excited": {"energy": 0.9, "valence": 0.85, "genre": "electronic"},
    "content": {"energy": 0.5, "valence": 0.6, "genre": "indie"},
    "neutral": {"energy": 0.5, "valence": 0.5, "genre": "alternative"},
    "sad": {"energy": 0.3, "valence": 0.3, "genre": "acoustic"},
    "very sad": {"energy": 0.2, "valence": 0.1, "genre": "slow"},
    "anxious": {"energy": 0.6, "valence": 0.4, "genre": "chill"},
    "bored": {"energy": 0.3, "valence": 0.5, "genre": "ambient"},
    "angry": {"energy": 0.9, "valence": 0.2, "genre": "metal"},
    "frustrated": {"energy": 0.8, "valence": 0.3, "genre": "punk"},
    "nostalgic": {"energy": 0.4, "valence": 0.6, "genre": "classic"},
    "romantic": {"energy": 0.5, "valence": 0.9, "genre": "R&B"},
}

# Using TextBlob to analyze user-entered mood's sentiment --> Done by Adi
def detect_mood(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    if sentiment.polarity > 0.5:
        return "happy"
    elif sentiment.polarity < -0.5:
        return "sad"
    else:
        return "neutral"

# using spotipy to recommend songs, shuffles the tracks to ensure recommendations are not the same every time --> Done by Adi
def recommend_songs(mood):
    if mood not in mood_data:
        mood = detect_mood(mood) 
    mood_info = mood_data[mood]
    results = sp.search(q=f'genre:{mood_info["genre"]}', type='track', limit=20)
    tracks = results['tracks']['items']
    random.shuffle(tracks)
    recommendations = []
    for track in tracks[:5]:
        recommendations.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'url': track['external_urls']['spotify']
        })
    
    return recommendations, mood_info

# Streamlit UI ('cuz it's easy to work with) --> Done by Rohan
st.title("🎵 Spotlight: Shine a Light on the Perfect Song for You")
mood_input = st.text_area("How are you feeling today? Describe your mood or enter a specific mood:")

if st.button("Get Recommendations"):
    if not mood_input:
        st.warning("Please describe your mood.")
    else:
        songs, mood_info = recommend_songs(mood_input)
        st.subheader(f"Songs for a {mood_input.title()} mood ({mood_info['genre'].title()} genre)")
        for song in songs:
            st.markdown(f"[{song['name']} by {song['artist']}]({song['url']})")
