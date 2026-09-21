"""Inference helpers.

Two modes are provided:
1. llama.cpp server over HTTP;
2. safe fallback message for demo UI.
"""
import os
import requests

def generate_with_llama_cpp(question: str, server_url: str | None = None) -> str:
    server_url = server_url or os.getenv("LLAMA_CPP_SERVER_URL", "http://127.0.0.1:8080")
    payload = {
        "prompt": question,
        "temperature": 0.1,
        "repeat_penalty": 1.3,
        "n_predict": 256,
    }
    response = requests.post(f"{server_url}/completion", json=payload, timeout=120)
    response.raise_for_status()
    data = response.json()
    return data.get("content", "").strip()

def demo_answer(question: str) -> str:
    return (
        "هاد الواجهة تجريبية. خاصك تربطها بالموديل المحلي ديالك "
        "باش تولد جواب فعلي للسؤال: " + question
    )
