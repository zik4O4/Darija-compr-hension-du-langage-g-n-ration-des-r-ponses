"""Prompt-format helpers.

Keep the semantic instruction consistent while adapting the wrapper to each model family.
"""

SYSTEM_PROMPT_AR = (
    "أنت مساعد طبي. أجب عن السؤال بدقة وبالدارجة المغربية، "
    "ولا تعتبر الجواب بديلاً عن استشارة طبيب."
)

def simple_instruction(question: str) -> str:
    return f"{SYSTEM_PROMPT_AR}\n\nالسؤال: {question}\nالجواب:"
