# PySlide - FAQ

## 1. Qu'est-ce que PySlide ?

PySlide est un framework Python conçu pour créer des présentations PowerPoint (`.pptx`) de manière rapide et simple, spécialement destiné aux développeurs qui préfèrent coder plutôt que d'utiliser des outils de présentation traditionnels comme PowerPoint.

___

## 2. Comment installer PySlide ?

Vous pouvez installer PySlide via pip en utilisant la commande suivante :

```bash
pip install pyslide
```

___

## 3. Comment créer une présentation de base avec PySlide ?

Vous pouvez trouver des [exemples](./examples/) dans le dossier `examples` du projet.

___

## 4. Pourquoi PySlide enregistre les présentations au format JSON ?

Voici les raisons principales :

1. **Simplicité de manipulation** : Le format JSON est facile à lire et à écrire, ce qui facilite la manipulation des données de la présentation.
2. **Parsabilité** : JSON est un format très simple à parser, ce qui permet une exportation PPTX plus simple à implémenter.
3. **Flemme de créer un nouveau format** : Oui, on avoue, on avait la flemme de créer un nouveau format de fichier spécifique pour PySlide.

___

## 5. Comment exporter une présentation JSON en fichier PPTX ?

Pour exporter une présentation JSON en fichier PPTX, vous pouvez utiliser la fonction `export_to_pptx` fournie par PySlide. Voici un exemple de code pour le faire :

```python
from pyslide.render.exportation.pptx import export_to_pptx

# supposons que vous avez déjà une présentation sauvegardée en JSON
export_to_pptx("ma_presentation.json", "ma_presentation.pptx")

# vous pouvez aussi exporter votre presentation directement sans passer par un fichier JSON
# pour cela, il faut avoir stocker votre presentation dans une variable
presentation = ...  # votre objet Presentation
export_to_pptx(presentation, "ma_presentation.pptx")
```

Vous pouvez également utiliser notre CLI (fortement recommandée) pour exporter vos présentations JSON en PPTX :

```bash
# Supposons que vous avez un fichier JSON nommé ma_presentation.json
cd mon_projet_pyslide
pyslide export --pptx ma_presentation.json ma_presentation.pptx

# Ou pour exporter directement une présentation Python
cd mon_projet_pyslide
pyslide export --pptx ma_presentation.py ma_presentation.pptx
```

___
