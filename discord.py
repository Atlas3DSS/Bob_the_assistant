def pull_discord_history(token):
    Client = discord.Client()
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    client.run(token)
    transcript_text = ""
    for guild in client.guilds:
        for channel in guild.text_channels:
            messages = await channel.history(limit=None).flatten()
            for message in messages:
                transcript_text += message.content + "\n"
    client.logout()
    return transcript_text

def poll_discord_daily():
    transcript_text = pull_discord_history(token)
    # Perform transcription and analysis on transcript_text
    embeddings = generate_embeddings(transcript_text)
    # Save embeddings to Embeddings folder
    embeddings_dir = "Embeddings"
    today = datetime.date.today().strftime("%Y-%m-%d")
    with open(os.path.join(embeddings_dir, today), 'w') as f:
        f.write(embeddings)

schedule.every().day.at("00:00").do(poll_discord_daily)

while True:
    schedule.run_pending()
    time.sleep(1)
