class Categoria():
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    
    def getNombre(self):
        return self.nombre


class Post(Categoria):
    
    def __init__(self, titulo, slug, detalle, media, categoria):
        self.titulo = titulo
        self.slug = slug
        self.detalle = detalle
        self.media = media
        self.categoria = categoria
        Categoria.__init__(self, "Juan Pérez")


p = Post("video 1", "video-1", "detalle del video", "media", "PHP")
print(p.getNombre())