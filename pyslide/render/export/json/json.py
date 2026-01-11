from pyslide import Presentation
from pyslide.elements import Title, Text, BulletList, InLineCodeBlock, MultiLineCodeBlock

import json

def save_to_json(filepath: str, filename: str):
    """Save data to a JSON file.
    
    Keyword arguments:
    filepath -- the path of the PySlide presentation to save
    filename -- the name of the json file to create
    Return: return_description
    """

    data = {
        "title": Presentation.title,
        "author": Presentation.author,
        "slides": []
    }

    for slide in Presentation.slides:
        slide_data = []

        for element in slide.elements:
            if isinstance(element, Title):
                slide_data.append({
                    "type": "Title",
                    "text": element.text
                })
            elif isinstance(element, BulletList):
                slide_data.append({
                    "type": "BulletList",
                    "items": element.items
                })
            elif isinstance(element, Text):
                slide_data.append({
                    "type": "Text",
                    "content": element.content
                })
            elif isinstance(element, InLineCodeBlock):
                slide_data.append({
                    "type": "InLineCodeBlock",
                    "code": element.code
                })
            elif isinstance(element, MultiLineCodeBlock):
                slide_data.append({
                    "type": "MultiLineCodeBlock",
                    "code": element.code
                })
        
        data["slides"].append(slide_data)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)