"""Training entry point for microsoft/Phi-3.5-mini-instruct.

Run on a CUDA GPU after installing the dependencies and accepting the model license if needed.
This file prints the training configuration by default. Add your exact dataset/prompt-loading
logic before launching a costly training run.
"""
from src.training.common import DecoderTrainingConfig, print_training_plan

MODEL_ID = "microsoft/Phi-3.5-mini-instruct"

def main():
    cfg = DecoderTrainingConfig(model_id=MODEL_ID, output_dir="outputs/phi")
    print_training_plan(cfg)

if __name__ == "__main__":
    main()
