# Push vers GitHub

## 1. Créer un dépôt vide sur GitHub

Nom conseillé :

```text
darija-medical-qa
```

Ne cochez pas l'option qui crée automatiquement un README si vous voulez pousser ce dossier tel quel.

## 2. Ouvrir le Terminal

```bash
cd chemin/vers/darija-medical-qa-complete
```

## 3. Initialiser Git

```bash
git init
git add .
git status
git commit -m "Initial commit: Darija Medical QA"
git branch -M main
```

## 4. Ajouter GitHub

```bash
git remote add origin https://github.com/TON_USERNAME/darija-medical-qa.git
git push -u origin main
```

## 5. Vérifier avant le push

Assurez-vous que Git ne contient pas :

- `.env`
- clés API
- token Hugging Face
- dataset privé
- checkpoints
- `.gguf`
- `.safetensors`
- `.bin`

Commande utile :

```bash
git status
```
