# TODO: Trouver un nom a ce fichier

from pyslide import Presentation, Slide
from pyslide.elements import (
    Title,
    Text,
    BulletList,
    InLineCodeBlock
)

prez = Presentation(
    title="Ma super presentation",
    author="Guillaume"
)
prez.add_slide(
    Slide(
        elements=[
            Title("Ma super presentation"),
            Text("Bienvenue dans ma super presentation !"),
            BulletList(
                items=[
                    InLineCodeBlock("Point 1"),
                    "Point 2",
                    "Point 3"
                ]
            )
        ]
    ),
    Slide(
        elements=[
            Title("Conclusion"),
            Text("Merci d'avoir assisté à ma super presentation !")
        ]
    )
)

# Sauvegarder la presentation en json
prez.save("ma_super_presentation.json")

# Exporter la presentation en pptx
prez.export("pptx")