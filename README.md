# PySlide - Le framework de ceux qui avaient la flemme d'ouvrir PowerPoint

_Vous aviez la flemme d'ouvrir PowerPoint ? PySlide est fait pour vous !_

Ce framework Python est conçu pour créer des présentations `pptx` très rapidement, de la manière la plus simple possible pour un dev !

## Installation

```bash
pip install pyslide
```

## Utilisation de base

Voici un exemple de base pour créer une présentation avec PySlide _(je vous recommande quand même de regarder les [exemples](./examples) dans le dossier `examples` car ils sont plus complets)_.

```python
from pyslide import Presentation, Slide
from pyslide.elements import Title, BulletList, MultiLineCodeBlock
```
