
openai.api_key = config.OPENAI_API_KEY

def transcribe(filepath):
    # load audio data
    audio = whisper.load_audio(filepath)

    # pad or trim audio to match desired length
    audio = whisper.pad_or_trim(audio)

    # compute log-mel spectrogram
    mel = whisper.log_mel_spectrogram(audio).to(device)

    # create decoding options
    options = whisper.DecodingOptions(language='en', fp16=False)

    # transcribe audio data
    result = whisper.decode(model, mel, options)

    # return transcription
    return result.text.strip()

if __name__ == "__main__":
    # set up directory paths and file names
    recordings_dir = 'recordings'
    model_path = 'base'
    trigger_words_file = 'trigger_words.txt'
    transcript_file = 'transcript.txt'

    # load pre-trained model
    model = whisper.load_model(model_path)

    # create file event handler
    event_handler = NewFileHandler(model, trigger_words_file)

    # create observer
    observer = Observer()

    # schedule event handler
    observer.schedule(event_handler, path=recordings_dir)

    # start observer
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

    # record audio data
    recorder.record()

    # sort audio data
    Sentiment.sort()

    # handle events
    EventHandler.event_handler()

# create Gradio user interface
ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="file", is_output_file=True), outputs="text")
ui.launch()
