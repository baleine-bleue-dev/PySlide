from pyslide import Presentation, Slide
from pyslide.elements import (
    Title,
    Text
)

# on crée une instance de Presentation qui stocke toute notre presentation
pres = Presentation(
    title="Presentation Simple",
    author="Moi"
)

# variable `slides` contenant une liste de slides
# ca nous permettra ensuite d'ajouter les slides un par un a la presentation avec `add_slide()`
slides = [
    Slide(
        elements=[
            Title("Slide 1"),
            Text("Ceci est la premiere slide.")
        ]
    ),
    Slide(
        elements=[
            Title("Slide 2"),
            Text("Ceci est la deuxieme slide.")
        ]
    )
]

# pour chaque slide dans la liste `slides`, on l'ajoute a la presentation avec `add_slide()`
for slide in slides:
    pres.add_slide(slide)

# on sauvegarde la presentation en json
pres.save("presentation_simple.json")
# on exporte la presentation en pptx
pres.export("presentation_simple.pptx")