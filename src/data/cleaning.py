"""Cleaning utilities for question-answer data."""
from pathlib import Path
import re
import pandas as pd

GENERIC_PATTERNS = [
    r"خاصك تشوف الطبيب",
    r"خاصو يشوف الطبيب",
    r"خصك تشوف الطبيب",
    r"شنو هو السؤال",
    r"لقيت الجواب",
]

def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", str(text)).strip()

def is_generic_answer(text: str) -> bool:
    text = normalize_spaces(text)
    return any(re.search(pattern, text) for pattern in GENERIC_PATTERNS)

def clean_dataframe(
    df: pd.DataFrame,
    question_col: str = "Question",
    answer_col: str = "Answer",
    min_words: int = 5,
    max_words: int = 80,
) -> pd.DataFrame:
    out = df.copy()
    out[question_col] = out[question_col].fillna("").map(normalize_spaces)
    out[answer_col] = out[answer_col].fillna("").map(normalize_spaces)

    out = out[(out[question_col] != "") & (out[answer_col] != "")]
    answer_len = out[answer_col].str.split().str.len()
    out = out[(answer_len >= min_words) & (answer_len <= max_words)]
    out = out[~out[answer_col].map(is_generic_answer)]
    out = out.drop_duplicates(subset=[question_col], keep="first")
    out = out.drop_duplicates(subset=[answer_col], keep="first")
    return out.reset_index(drop=True)

def main():
    root = Path(__file__).resolve().parents[2]
    inp = root / "data" / "samples" / "sample_medqa_synthetic.csv"
    outp = root / "data" / "processed" / "medqa_cleaned_synthetic.csv"
    df = pd.read_csv(inp)
    cleaned = clean_dataframe(df)
    cleaned.to_csv(outp, index=False, encoding="utf-8-sig")
    print(f"Input rows: {len(df)}")
    print(f"Clean rows: {len(cleaned)}")
    print(f"Saved to: {outp}")

if __name__ == "__main__":
    main()
