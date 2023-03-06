def load_transcripts():
    transcripts_dir = "transcripts"
    today = datetime.date.today().strftime("%Y-%m-%d")
    transcript_files = [os.path.join(transcripts_dir, f) for f in os.listdir(transcripts_dir) if f.startswith(today)]
    transcript_text = ""
    for file in transcript_files:
        with open(file) as f:
            transcript_text += f.read() + "\n"
    return transcript_text
