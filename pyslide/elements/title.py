from . import Element

class Title(Element):
    def __init__(self, text: str, style: dict | None):
        super().__init__()
        self.text = text
        self.style = style