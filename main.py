import sounddevice as sd
import wavio as wv
import datetime
import gradio as gr
import numpy as np
import openai, config
import recorder
import Sorter
import Transcriber
import config
import whisper
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from new_file_handler import NewFileHandler

if __name__ == "__main__":
    recordings_dir = os.path.join('recordings')

    model = whisper.load_model("base")
    trigger_words_file = "trigger_words.txt"

    event_handler = NewFileHandler(model, trigger_words_file)
    observer = Observer()
    observer.schedule(event_handler, path=recordings_dir)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()