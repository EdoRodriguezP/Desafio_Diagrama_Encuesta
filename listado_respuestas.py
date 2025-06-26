class ListadoRespuestas:
    #Almacena las respuestas de un usuario a una encuesta.
    def __init__(self, usuario, respuestas: list):
        self._usuario = usuario
        self._respuestas = respuestas

    @property
    def usuario(self):
        # Devuelve el usuario que respondió la encuesta
        return self._usuario

    @property
    def respuestas(self):
        # Devuelve la lista de respuestas del usuario
        return self._respuestas
