def composite_score(bertscore_f1: float, chrf: float, accuracy_05: float, rouge_l: float) -> float:
    return (
        0.35 * bertscore_f1
        + 0.25 * chrf
        + 0.25 * accuracy_05
        + 0.15 * rouge_l
    )

def accuracy_at_threshold(similarities, threshold: float = 0.5) -> float:
    if not similarities:
        return 0.0
    return sum(float(s >= threshold) for s in similarities) / len(similarities)
