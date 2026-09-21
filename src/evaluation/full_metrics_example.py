"""Optional metric-computation example.

This script demonstrates how the packages can be wired together.
It is intentionally not executed automatically because BERTScore and sentence
embeddings may download large models.
"""
from typing import List

def compute_chrf(predictions: List[str], references: List[str]):
    import sacrebleu
    scores = [
        sacrebleu.sentence_chrf(p, [r]).score / 100.0
        for p, r in zip(predictions, references)
    ]
    return sum(scores) / len(scores)

def compute_rouge_l(predictions: List[str], references: List[str]):
    from rouge_score import rouge_scorer
    scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=False)
    vals = [scorer.score(r, p)["rougeL"].fmeasure for p, r in zip(predictions, references)]
    return sum(vals) / len(vals)

def compute_bertscore_f1(predictions: List[str], references: List[str], lang="ar"):
    from bert_score import score
    _, _, f1 = score(predictions, references, lang=lang, verbose=False)
    return float(f1.mean())
