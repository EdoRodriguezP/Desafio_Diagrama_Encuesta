class Alternativa:
    def __init__(self, contenido: str, ayuda: str):
        # Inicializa una alternativa con contenido y ayuda opcional
        self._contenido = contenido
        self._ayuda = ayuda

    @property
    def contenido(self):
        # Permite obtener el contenido de la alternativa
        return self._contenido

    @contenido.setter
    def contenido(self, valor):
        # Permite modificar el contenido de la alternativa
        self._contenido = valor

    @property
    def ayuda(self):
        # Permite obtener la ayuda de la alternativa
        return self._ayuda

    @ayuda.setter
    def ayuda(self, valor):
        # Permite modificar la ayuda de la alternativa
        self._ayuda = valor

    def mostrar(self):
        # Devuelve un string con el contenido y, si existe, la ayuda de la alternativa
        if self._ayuda:
            return f"{self._contenido} (Ayuda: {self._ayuda})"
        return self._contenido

