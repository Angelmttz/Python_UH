class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_informacion(self):
        """
        Muestra el libro.
        """
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")


mi_libro = Libro(titulo="Wigetta", autor="willirex y vegetta777", paginas=100)
mi_libro.mostrar_informacion()


