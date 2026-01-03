from . import Element

class MultiLineCodeBlock(Element):
    def __init__(self, code: str, style: dict | None):
        super().__init__()
        self.code = code
        self.style = style

class InLineCodeBlock(Element):
    def __init__(self, code: str, style: dict | None):
        super().__init__()
        self.code = code
        self.style = style