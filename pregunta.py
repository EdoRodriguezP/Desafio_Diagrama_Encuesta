from alternativa import Alternativa  # Importa la clase Alternativa para usarla en la pregunta

class Pregunta:
    def __init__(self, enunciado: str, ayuda: str, requerida: bool = False, alternativas: list = []):
        # Inicializa la pregunta con enunciado, ayuda, si es requerida y una lista de alternativas
        self._enunciado = enunciado  
        self._ayuda = ayuda          
        self._requerida = requerida  
        # Crea objetos Alternativa a partir de la lista de diccionarios recibida
        self._alternativas = [Alternativa(**alt) for alt in (alternativas or [])]

    @property
    def enunciado(self):
        # Permite obtener el enunciado de la pregunta
        return self._enunciado

    @enunciado.setter
    def enunciado(self, valor):
        # Permite modificar el enunciado de la pregunta
        self._enunciado = valor

    @property
    def ayuda(self):
        # Permite obtener la ayuda de la pregunta
        return self._ayuda

    @ayuda.setter
    def ayuda(self, valor):
        # Permite modificar la ayuda de la pregunta
        self._ayuda = valor

    @property
    def requerida(self):
        # Permite saber si la pregunta es requerida
        return self._requerida

    @requerida.setter
    def requerida(self, valor):
        # Permite modificar si la pregunta es requerida
        self._requerida = valor

    @property
    def alternativas(self):
        # Permite obtener la lista de alternativas de la pregunta
        return self._alternativas

    def mostrar(self):
        # Devuelve un string con el enunciado, ayuda (si existe) y las alternativas
        texto = self._enunciado  # Comienza el texto con el enunciado de la pregunta
        if self._ayuda:  # Si hay ayuda, la agrega al texto
            texto += f" (Ayuda: {self._ayuda})"
        texto += "\nAlternativas:"  # Agrega el título para las alternativas
        for alt in self._alternativas:  # Recorre cada alternativa de la pregunta
            texto += f"\n- {alt.mostrar()}"  # Usa el método mostrar de Alternativa para mostrar su contenido y ayuda
        return texto  # Devuelve el texto completo con enunciado, ayuda y alternativas
