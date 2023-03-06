if __name__ == "__main__":
    from imports import *

    openai.api_key = config.OPENAI_API_KEY
    client = discord.Client()

    recordings_dir = os.path.join('recordings')
    #open the latest recording file
    latest_recording = sorted(os.listdir(recordings_dir))[-1]
    latest_recording_path = os.path.join(recordings_dir, latest_recording)
    
    #load the model
    model = whisper.load_model("base")
    trigger_words_file = "trigger_words.txt"
    
    #create an event handler
    event_handler = NewFileHandler(model, trigger_words_file)
    
    #create an observer
    observer = Observer()
    
    #schedule the event handler
    observer.schedule(event_handler, path=recordings_dir)
    
    #start the observer
    observer.start()
    
    #this is the main loop
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
    recorder.record()
    Sentiment.sort()
    EventHandler.event_handler()

    ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text")
    ui.launch()
