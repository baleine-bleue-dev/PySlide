from pyslide.presentation import Presentation
from pyslide.elements import Title, Text, BulletList, InLineCodeBlock, MultiLineCodeBlock

def export_to_pptx(presentation: Presentation, filename: str):
    print(f"Exporting presentation '{presentation.title}' to {filename}...")
    pass   # pour l implementation de l exportation pptx on verra plus tard

def render_element_pptx(element, pptx_slide):
    if isinstance(element, Title):
        # creer le xml du titre
        pass
    elif isinstance(element, Text):
        # creer le xml du texte
        pass
    elif isinstance(element, BulletList):
        # creer le xml de la liste a puces
        pass
    elif isinstance(element, InLineCodeBlock):
        # creer le xml du code en ligne
        pass
    elif isinstance(element, MultiLineCodeBlock):
        # creer le xml du bloc de code multilignes
        pass