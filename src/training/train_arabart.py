"""AraBART full fine-tuning entry point."""
MODEL_ID = "moussaKam/AraBART"

CONFIG = {
    "learning_rate": 3e-5,
    "num_train_epochs": 3,
    "max_length": 256,
}

def main():
    print("Model:", MODEL_ID)
    print("Strategy: full fine-tuning")
    print(CONFIG)
    print("Connect this script to your real train/validation dataset before training.")

if __name__ == "__main__":
    main()
