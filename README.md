# Darija Medical QA

Projet académique de **Question Answering médical en Darija marocaine**.

Ce dépôt fournit une structure complète et reproductible pour :

- analyser et nettoyer des paires question-réponse ;
- préparer des ensembles train / validation / test ;
- adapter des modèles Transformer ;
- comparer Atlas-Chat, Llama 3.1, Mistral 7B, Phi-3.5 Mini et AraBART ;
- générer des réponses ;
- calculer BERTScore, chrF, Accuracy@0.5, ROUGE-L et un score composite ;
- lancer une petite interface Streamlit.

> **Important**
>
> Les fichiers de données inclus dans ce dépôt sont **des exemples synthétiques créés pour la structure du projet**.
> Ils ne reproduisent pas le corpus MedQA-MA original.
> Le vrai corpus doit être obtenu depuis sa source officielle et utilisé conformément à sa licence.

## Structure

```text
darija-medical-qa-complete/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── PUSH_TO_GITHUB.md
├── notebooks/
├── data/
│   ├── raw/
│   ├── processed/
│   └── samples/
├── src/
│   ├── data/
│   ├── training/
│   ├── evaluation/
│   └── inference/
├── app/
├── results/
├── figures/
├── docs/
└── models/
```

## Méthodologie représentée

Les modèles Decoder-only sont prévus pour une adaptation **SFT + QLoRA**.
AraBART est prévu pour un **Fine-Tuning complet**.

Configuration expérimentale représentée dans les scripts :

- LoRA `r = 16`
- LoRA `alpha = 32`
- LoRA dropout `0.05`
- Decoder-only : `1` époque
- Learning rate Decoder-only : `2e-4`
- AraBART : `3` époques
- Learning rate AraBART : `3e-5`
- Longueur maximale : `256` tokens
- Batch size par appareil : `4`
- Gradient accumulation : `4`
- Seed : `42`

## Résultats du mémoire

Les fichiers `results/preselection_results.csv` et `results/final_results.csv` contiennent les valeurs rapportées dans le mémoire.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Préparation des données d'exemple

```bash
python -m src.data.prepare_demo_data
```

## Nettoyage

```bash
python -m src.data.cleaning
```

## Évaluation du score composite

```bash
python -m src.evaluation.evaluate
```

## Interface Streamlit

```bash
streamlit run app/app.py
```

L'interface fournie est une interface de démonstration.
Elle ne charge pas automatiquement un modèle de plusieurs milliards de paramètres.
Pour une vraie inférence, configurez `MODEL_PATH` et adaptez `src/inference/generate.py`.

## Données et modèles volumineux

Ne poussez pas sur GitHub :

- checkpoints ;
- fichiers `.gguf` ;
- fichiers `.safetensors` ;
- modèles téléchargés ;
- corpus privé ou soumis à restrictions ;
- tokens et clés API.

## Avertissement médical

Ce projet est académique et expérimental.
Les réponses générées ne remplacent pas l'avis, le diagnostic ou le traitement d'un professionnel de santé.

## Auteur

Zakariya BEN KASSI

Projet de fin d'études — Intelligence Artificielle.
