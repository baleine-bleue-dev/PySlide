def save_to_json(data: dict, filename: str):    # NOTE: le format json est utilisé pour sauvegarder les diapo generés. C est le format par defaut d enregistrement de PySlide
    import json
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)