def finetune_bob(embeddings):
    model_id = config.GPT3_MODEL_ID
    model = openai.api.Model.retrieve(model_id)

    model.finetune(
        training_data=[
            {
                "text": e,
                "metadata": {
                    "response": ""
                }
            } for e in embeddings
        ],
        epochs=10,
        batch_size=64,
        learning_rate=1e-5,
        validation_split=0.2
    )

def monthly_finetune():
    embeddings = # retrieve embeddings from previous month's transcripts
    finetune_bob(embeddings)

# Schedule job to run on the first day of every month at 12:00 PM
schedule.every().month.at('12:00').do(monthly_finetune)

while True:
    schedule.run_pending()
    time.sleep(1)
