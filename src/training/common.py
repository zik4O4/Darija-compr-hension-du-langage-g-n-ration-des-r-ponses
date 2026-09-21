"""Common QLoRA training utilities.

These functions are written as a reusable starting point.
Actual large-model training requires GPU resources and access to model weights.
"""
from dataclasses import dataclass

@dataclass
class DecoderTrainingConfig:
    model_id: str
    output_dir: str
    learning_rate: float = 2e-4
    num_train_epochs: int = 1
    max_length: int = 256
    per_device_train_batch_size: int = 4
    gradient_accumulation_steps: int = 4
    weight_decay: float = 0.01
    warmup_steps: int = 100
    lora_r: int = 16
    lora_alpha: int = 32
    lora_dropout: float = 0.05

def print_training_plan(cfg: DecoderTrainingConfig):
    print("Model:", cfg.model_id)
    print("Output:", cfg.output_dir)
    print("QLoRA: 4-bit NF4")
    print("LoRA r / alpha / dropout:", cfg.lora_r, cfg.lora_alpha, cfg.lora_dropout)
    print("LR:", cfg.learning_rate)
    print("Epochs:", cfg.num_train_epochs)
    print("Max length:", cfg.max_length)
