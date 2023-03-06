def finetune_bob(embeddings):
    model = openai.api.Model.retrieve("your-model-id-here")
    model.finetune(
        examples=[{"input": e, "output": "response"} for e in embeddings],
        epochs=10,
        batch_size=64,
        learning_rate=1e-5,
        validation_split=0.2
    )
