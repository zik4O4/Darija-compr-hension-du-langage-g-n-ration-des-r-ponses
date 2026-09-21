# Méthodologie

## 1. Données

Le pipeline attendu est :

1. chargement du corpus ;
2. normalisation des espaces ;
3. suppression des entrées vides ;
4. filtrage des réponses trop courtes ou trop longues ;
5. filtrage de formulations génériques non informatives ;
6. déduplication ;
7. découpage train / validation / test.

Les données incluses dans ce dépôt sont synthétiques et servent uniquement à tester le pipeline.

## 2. Modèles

- Atlas-Chat — Decoder-only
- Llama 3.1 — Decoder-only
- Mistral 7B — Decoder-only
- Phi-3.5 Mini — Decoder-only
- AraBART — Encoder-Decoder

## 3. Adaptation

Decoder-only :
- Supervised Fine-Tuning
- QLoRA
- quantification 4 bits NF4
- LoRA sur les projections d'attention et de MLP

AraBART :
- Fine-Tuning complet
- apprentissage séquence-à-séquence

## 4. Évaluation

Métriques :
- BERTScore F1
- chrF
- Accuracy@0.5 sur similarité sémantique
- ROUGE-L

Score composite :

```text
0.35 * BERTScore_F1
+ 0.25 * chrF
+ 0.25 * Accuracy@0.5
+ 0.15 * ROUGE-L
```

## 5. Protocole en deux phases

Phase 1 :
- présélection de cinq modèles sur un sous-ensemble.

Phase 2 :
- reprise des modèles retenus depuis leur modèle de base ;
- entraînement complet ;
- évaluation finale sur l'ensemble de test complet.
