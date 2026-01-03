from pyslide.elements import Title, Text, BulletList, InLineCodeBlock, MultiLineCodeBlock

def render_element_terminal(element):
    if isinstance(element, Title):
        print(f"\n=== {element.text} ===\n")
    elif isinstance(element, Text):
        print("\n", element.content)
    elif isinstance(element, BulletList):
        print()
        for item in element.items:
            print(f" • {item}")
    elif isinstance(element, InLineCodeBlock):
        print(f"`{element.code}`", end=' ')
    elif isinstance(element, MultiLineCodeBlock):
        print("\n```\n" + element.code + "\n```")