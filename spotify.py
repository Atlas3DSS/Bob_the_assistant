scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def pull_spotify_history():
    response = sp.current_user_recently_played()
    transcript_text = ""
    for item in response['items']:
        track = item['track']
        transcript_text += f"{track['artists'][0]['name']} - {track['name']}\n"
    return transcript_text

def generate_embeddings(text):
    model_engine = "text-davinci-002"
    input_text = text
    output_format = "json"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=input_text,
        temperature=0.7,
        max_tokens=1024,
        n = 1,
        stop=None,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        echo=False,
        logprobs=10,
        user=None,
        models=None,
        model_bias=None,
        metadata=None,
        webhook_url=None,
        **{"stop_sequence": "\n\n"}
    )

    embeddings = np.array(response.choices[0].text.split("\n\n")[:-1])
    embeddings = embeddings.astype(np.float)
    embeddings = np.mean(embeddings, axis=0)
    embeddings = embeddings.tolist()

    return embeddings
