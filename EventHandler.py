openai.api_key = config.OPENAI_API_KEY

def transcribe(filepath):
    # Load audio data
    audio = whisper.load_audio(filepath)

    # Pad or trim audio to match desired length
    audio = whisper.pad_or_trim(audio)

    # Compute log-mel spectrogram
    mel = whisper.log_mel_spectrogram(audio).to(device)

    # Create decoding options
    options = whisper.DecodingOptions(language='en', fp16=False)

    # Transcribe audio data
    result = whisper.decode(model, mel, options)

    # Check if "bob" was mentioned in transcription
    if "bob" in result.text.lower():
        # Generate a dynamic message for Bob
        messages = [result.text.strip()]
        prompts = ["What's your question, boss?", "What's on your mind today?", "How can I assist you?"]
        prompt = random.choice(prompts)
        messages.append(prompt)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="\n".join(messages),
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Speak the generated message using text-to-speech
        engine = pyttsx3.init()
        engine.say(response.choices[0].text)
        engine.runAndWait()

    # Return transcription
    return result.text.strip()


if __name__ == "__main__":
    # Set up directory paths and file names
    recordings_dir = 'recordings'
    model_path = 'base'
    trigger_words_file = 'trigger_words.txt'
    transcript_file = 'transcript.txt'

    # Load pre-trained model
    model = whisper.load_model(model_path)

    # Create file event handler
    event_handler = NewFileHandler(model, trigger_words_file)

    # Create observer
    observer = Observer()

    # Schedule event handler
    observer.schedule(event_handler, path=recordings_dir)

    # Start observer
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

    # Record audio data
    recorder.record()

    # Sort audio data
    Sentiment.sort()

    # Handle events
    EventHandler.event_handler()

    # Create Gradio user interface
    ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="file", is_output_file=True), outputs="text")
    ui.launch()
