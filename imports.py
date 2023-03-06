import sounddevice as sd
import wavio as wv
import datetime
import gradio as gr
import numpy as np
import recorder
import Sentiment
import EventHandler
import nltk
import nltk.sentiment.vader as vader
from nltk.corpus import stopwords
import schedule
import discord
import time
import openai
import config
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from new_file_handler import NewFileHandler
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import pyttsx3
import os
import datetime
import whisper
openai.api_key = config.OPENAI_API_KEY