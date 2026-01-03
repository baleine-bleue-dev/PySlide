from .elements import Element
from .render.terminal.terminal import render_element_terminal
from .render.exportation.pptx.pptx import render_element_pptx

class Slide:
    def __init__(self, elements: list[Element], id: int):
        self.elements = elements
        self.id = id
    
    def render_terminal(self):
        for element in self.elements:
            render_element_terminal(element)
    
    def render_pptx(self, slide_xml):
        for element in self.elements:
            render_element_pptx(element, slide_xml)