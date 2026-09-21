SEED = 42

DECODER_CONFIG = {
    "lora_r": 16,
    "lora_alpha": 32,
    "lora_dropout": 0.05,
    "learning_rate": 2e-4,
    "epochs": 1,
    "max_length": 256,
    "per_device_train_batch_size": 4,
    "gradient_accumulation_steps": 4,
    "weight_decay": 0.01,
    "warmup_steps": 100,
}

ARABART_CONFIG = {
    "learning_rate": 3e-5,
    "epochs": 3,
    "max_length": 256,
}
