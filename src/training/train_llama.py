"""Training entry point for meta-llama/Meta-Llama-3.1-8B-Instruct.

Run on a CUDA GPU after installing the dependencies and accepting the model license if needed.
This file prints the training configuration by default. Add your exact dataset/prompt-loading
logic before launching a costly training run.
"""
from src.training.common import DecoderTrainingConfig, print_training_plan

MODEL_ID = "meta-llama/Meta-Llama-3.1-8B-Instruct"

def main():
    cfg = DecoderTrainingConfig(model_id=MODEL_ID, output_dir="outputs/llama")
    print_training_plan(cfg)

if __name__ == "__main__":
    main()
