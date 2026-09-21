from pathlib import Path
import pandas as pd
from src.evaluation.metrics import composite_score

def main():
    root = Path(__file__).resolve().parents[2]
    results_path = root / "results" / "final_results.csv"
    df = pd.read_csv(results_path)
    df["Composite_Recomputed"] = df.apply(
        lambda r: composite_score(
            r["BERTScore_F1"], r["chrF"], r["Accuracy@0.5"], r["ROUGE-L"]
        ),
        axis=1,
    )
    print(df.to_string(index=False))

if __name__ == "__main__":
    main()
