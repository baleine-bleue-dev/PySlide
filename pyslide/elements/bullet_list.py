from . import Element
from ..utils.generate_id import generate_id

class BulletList(Element()):
    def __init__(self, items: list, style: dict | None, id: str):
        super().__init__()
        self.items = items
        self.style = style
        self.id = id