from . import Element

class Text(Element):
    def __init__(self, content: str, style: dict | None):
        super().__init__()
        self.content = content
        self.style = style