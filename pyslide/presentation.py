class Presentation:
    def __init__(self, title, author, id: str | None):
        self.title = title
        self.author = author
        self.slides = []
        self.id = id if id is not None else self.generate_id()

    def add_slide(self, slide):
        self.slides.append(slide)

    # Permet de sauvegarder la presentation dans un fichier json (le format d enregistrement par defaut de PySlide)
    def save(self, filename: str):
        from .utils.save_to_json import save_to_json
        data = {
            "title": self.title,
            "author": self.author,
            "slides": [slide.id for slide in self.slides]
        }
        save_to_json(data, filename)

    def present(self):
        pass    # pour l implementation de la presentation dans le terminal on verra plus tard

    def preview(self):
        pass    # pour l implementation de l apercu gui on verra plus tard

    def export(self, format):
        if format == "pptx":
            from .render.exportation.pptx.pptx import export_to_pptx
            print("Exportation en PPTX...")
            export_to_pptx(self, f"{self.title}.pptx")
        else:
            print(f"Format {format} non pris en charge.")
            pass    # pour l implementation de l exportation on verra plus tard