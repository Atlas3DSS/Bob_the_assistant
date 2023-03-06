# Set up OpenAI API key
openai.api_key = config.OPENAI_API_KEY

# Set up trigger words
with open("trigger_words.txt", "r") as f:
    trigger_words = [line.strip() for line in f.readlines()]

# Set up directory for recordings
recordings_dir = os.path.join(os.getcwd(), 'recordings')

# Set up model and event handler for trigger words
model = whisper.load_model("base")
event_handler = EventHandler.NewFileHandler(model, trigger_words)

# Set up observer for new recordings
observer = EventHandler.Observer()
observer.schedule(event_handler, path=recordings_dir)
observer.start()

# Function to start recording audio
def start_recording():
    freq = 44100
    duration = 5 # in seconds
    print('Recording')
    while True:
        ts = datetime.datetime.now()
        filename = ts.strftime("%Y-%m-%d %H:%M:%S")
        # Start recorder with the given values of duration and sample frequency
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
        # Record audio for the given number of seconds
        sd.wait()
        # Convert the NumPy array to audio file
        wv.write(f"{recordings_dir}/{filename}.wav", recording, freq, sampwidth=2)

# Function to transcribe audio and return sentiment analysis
def transcribe_and_analyze(audio_file):
    # Perform transcription
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    # Perform sentiment analysis
    sentiment = Sentiment.get_sentiment(transcript["text"])
    # Return transcript and sentiment
    return {"transcript": transcript["text"], "sentiment": sentiment}

# Gradio interface
audio_input = gr.inputs.Audio(source="microphone")
recording_toggle = gr.inputs.Checkbox(label="Start/stop recording")
transcription_output = gr.outputs.Textbox(label="Transcription")
sentiment_output = gr.outputs.Textbox(label="Sentiment")

def interface(audio, recording_toggle):
    # If recording toggle is on, start recording
    if recording_toggle:
        start_recording()
    # If recording toggle is off, get latest recording and perform transcription and sentiment analysis
    else:
        # Get path of latest audio file
        latest_recording = sorted(os.listdir(recordings_dir))[-1]
        latest_recording_path = os.path.join(recordings_dir, latest_recording)
        # Perform transcription and sentiment analysis
        results = transcribe_and_analyze(latest_recording_path)
        # Call event handler to perform actions based on trigger words
        event_handler.on_created(latest_recording_path)
        # Return transcript and sentiment analysis
        return {"Transcription": results["transcript"], "Sentiment": results["sentiment"]}

gr.Interface(fn=interface, inputs=[audio_input, recording_toggle], outputs=[transcription_output, sentiment_output], title="My AI Assistant", description="Record and transcribe audio, and perform sentiment analysis and actions based on trigger words.").launch()
