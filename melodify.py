import spotipy
from spotipy.oauth2 import SpotifyOAuth
from textblob import TextBlob

CLIENT_ID = 'b738762f62eb432cb9e9b781d884384b'
CLIENT_SECRET = '5007b396aaa345d5be1bd211479cbd66'
REDIRECT_URI = "http://localhost:8888/callback"

scope = 'user-library-read playlist-read-private user-modify-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))

## The above code was written by Adi

mood_to_features = {
    "very happy": {"energy": 0.9, "valence": 0.9},
    "happy": {"energy": 0.8, "valence": 0.8},
    "excited": {"energy": 0.9, "valence": 0.85},
    "content": {"energy": 0.5, "valence": 0.6},
    "neutral": {"energy": 0.5, "valence": 0.5},
    "sad": {"energy": 0.3, "valence": 0.3},
    "very sad": {"energy": 0.2, "valence": 0.1},
    "anxious": {"energy": 0.6, "valence": 0.4},
    "bored": {"energy": 0.3, "valence": 0.5},
    "angry": {"energy": 0.9, "valence": 0.2},
    "frustrated": {"energy": 0.8, "valence": 0.3},
    "nostalgic": {"energy": 0.4, "valence": 0.6},
    "romantic": {"energy": 0.5, "valence": 0.9},
}

mood_to_genre = {
    "very happy": "dance",
    "happy": "pop",
    "excited": "electronic",
    "content": "indie",
    "neutral": "alternative",
    "sad": "acoustic",
    "very sad": "slow",
    "anxious": "chill",
    "bored": "ambient",
    "angry": "metal",
    "frustrated": "punk",
    "nostalgic": "classic",
    "romantic": "R&B",
}

## Mapping mood to features and genre was done by Rohan

## The functions were defined by Adi

def detect_mood(user_input):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.6:
        return "very happy"
    elif polarity > 0.2:
        return "happy"
    elif polarity > 0.0:
        return "excited"
    elif polarity >= -0.2:
        return "neutral"
    elif polarity > -0.6:
        return "sad"
    else:
        return "very sad"

def recommended_songs(mood, energy, valence, sp):
    genre = mood_to_genre.get(mood, "pop")
    query_params = {
        'seed_genres': genre,
        'target_energy': energy,
        'target_valence': valence,
        'limit': 10
    }
    recommendations = sp.recommendations(**query_params)
    recommended_songs = []

# We got kinda lazy we'll complete this eventually :)
