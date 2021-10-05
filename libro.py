class Libro:
    def __init__(self, titulo, revisiones, año, idioma, rating, isbn):
        self.titulo = titulo
        self.revisiones = int(revisiones)
        self.año = año
        self.idioma = idioma
        self.rating = float(rating)
        self.isbn = isbn

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.titulo, self.revisiones, self.año, self.idioma, self.rating, self.isbn)