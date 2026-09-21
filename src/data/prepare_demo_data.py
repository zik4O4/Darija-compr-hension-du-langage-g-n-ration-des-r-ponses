from pathlib import Path
import pandas as pd

def main():
    root = Path(__file__).resolve().parents[2]
    sample = root / "data" / "samples" / "sample_medqa_synthetic.csv"
    df = pd.read_csv(sample)
    print(df.head())
    print(f"Rows: {len(df)}")
    print("This is synthetic demonstration data, not the original MedQA-MA corpus.")

if __name__ == "__main__":
    main()
