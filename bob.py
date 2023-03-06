messages = [{"role": "system", "content": "You are Bob a chat bot, You are helpful and friendly. You are verbose. You are a polymath. You are a nerd. You are sarcastic. Wherever possible You are a utilitarian with a strong perference for individual libtery and free enterprise."}]

def bob(audio_file):
    global messages

    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    engine = pyttsx3.init()
    engine.say(system_message['content'])
    engine.runAndWait()

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript

def handle_bob_trigger():
    # get path of latest audio file
    latest_recording = sorted(os.listdir('recordings'))[-1]
    latest_recording_path = os.path.join('recordings', latest_recording)

    # invoke bob function with latest audio file as argument
    with open(latest_recording_path, 'rb') as audio_file:
        chat_transcript = bob(audio_file)

    # do something with chat_transcript (e.g., save to disk, display in UI, etc.)
