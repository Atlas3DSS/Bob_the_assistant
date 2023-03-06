def generate_embeddings(transcript_text):
    openai.api_key = config.OPENAI_API_KEY
    pipeline = openai.api.Pipeline(model="text-davinci-002", task="text-embedding")
    response = pipeline([transcript_text])
    embeddings = response['data'][0]['embedding']

    # Create daily folder
    daily_folder = os.path.join('Embeddings', datetime.date.today().strftime('%Y-%m-%d'))
    os.makedirs(daily_folder, exist_ok=True)

    # Write embeddings to file
    with open(os.path.join(daily_folder, 'embeddings.txt'), 'w') as f:
        f.write(str(embeddings))

    # Log success
    with open(os.path.join(daily_folder, 'log.txt'), 'w') as f:
        f.write('Embeddings generated successfully.')

    return embeddings
