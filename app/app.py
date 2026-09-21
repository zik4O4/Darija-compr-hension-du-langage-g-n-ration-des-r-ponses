import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from src.inference.generate import demo_answer, generate_with_llama_cpp

st.set_page_config(page_title="Darija Medical QA", page_icon="🩺")
st.title("Darija Medical QA")
st.caption("Prototype académique de Question Answering médical en Darija")

mode = st.sidebar.selectbox(
    "Mode d'inférence",
    ["Démonstration", "llama.cpp server"],
)

question = st.text_area(
    "دخل السؤال الطبي بالدارجة المغربية",
    placeholder="مثال: واش الصداع ديما كيعني شي مرض خطير؟",
)

if st.button("Générer"):
    if not question.strip():
        st.warning("Veuillez saisir une question.")
    else:
        try:
            if mode == "llama.cpp server":
                answer = generate_with_llama_cpp(question)
            else:
                answer = demo_answer(question)
            st.markdown("### Réponse")
            st.write(answer)
        except Exception as exc:
            st.error(f"Erreur d'inférence : {exc}")

st.divider()
st.warning(
    "Projet académique et expérimental. Les réponses ne remplacent pas l'avis, "
    "le diagnostic ou le traitement d'un professionnel de santé."
)
