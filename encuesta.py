from pregunta import Pregunta

class Encuesta:
    """
    Representa una encuesta con un nombre, preguntas y respuestas de usuarios.
    """
    def __init__(self, nombre: str, preguntas: list ):
        self._nombre = nombre
        # Crea objetos Pregunta a partir de los datos recibidos
        self._preguntas = [Pregunta(**preg) for preg in (preguntas or [])]
        self._listados_respuestas = []

    @property
    def nombre(self):
        # Devuelve el nombre de la encuesta
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        # Permite modificar el nombre de la encuesta
        self._nombre = valor

    @property
    def preguntas(self):
        # Devuelve la lista de preguntas de la encuesta
        return self._preguntas

    @property
    def listados_respuestas(self):
        # Devuelve los listados de respuestas de los usuarios
        return self._listados_respuestas

    def mostrar(self):
        """
        Devuelve un string con la información de la encuesta y sus preguntas.
        """
        texto = f"Encuesta: {self._nombre}\n"
        for preg in self._preguntas:
            texto += preg.mostrar() + "\n"
        return texto

    def agregar_listado_respuestas(self, listado):
        """
        Agrega un listado de respuestas a la encuesta.
        """
        self._listados_respuestas.append(listado)

class EncuestaLimitadaEdad(Encuesta):
    """
    Encuesta que solo acepta respuestas de usuarios dentro de un rango de edad.
    """
    def __init__(self, nombre, preguntas, edad_min=0, edad_max=120):
        super().__init__(nombre, preguntas)
        self._edad_min = edad_min
        self._edad_max = edad_max

    @property
    def edad_min(self):
        return self._edad_min

    @edad_min.setter
    def edad_min(self, valor):
        # Solo permite establecer un valor válido para edad mínima
        if 0 <= valor <= self._edad_max:
            self._edad_min = valor

    @property
    def edad_max(self):
        return self._edad_max

    @edad_max.setter
    def edad_max(self, valor):
        # Solo permite establecer un valor válido para edad máxima
        if valor >= self._edad_min:
            self._edad_max = valor

    def agregar_listado_respuestas(self, listado):
        """
        Agrega el listado de respuestas solo si el usuario está dentro del rango de edad permitido.
        """
        usuario = listado.usuario
        if self._edad_min <= usuario.edad <= self._edad_max:
            self._listados_respuestas.append(listado)

class EncuestaLimitadaRegion(Encuesta):
    """
    Encuesta que solo acepta respuestas de usuarios de ciertas regiones.
    """
    def __init__(self, nombre, preguntas, regiones=None):
        super().__init__(nombre, preguntas)
        self._regiones = regiones or []

    @property
    def regiones(self):
        return self._regiones

    @regiones.setter
    def regiones(self, valor):
        # Solo permite establecer una lista de regiones válida
        if isinstance(valor, list):
            self._regiones = valor

    def agregar_listado_respuestas(self, listado):
        """
        Agrega el listado de respuestas solo si el usuario pertenece a una región permitida.
        """
        usuario = listado.usuario
        if usuario.region in self._regiones:
            self._listados_respuestas.append(listado)
