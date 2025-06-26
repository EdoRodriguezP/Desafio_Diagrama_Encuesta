from listado_respuestas import ListadoRespuestas

class Usuario:
    """
    Representa a un usuario que puede contestar encuestas.
    """
    def __init__(self, correo: str, edad: int, region: int):
        self._correo = correo
        self._edad = edad
        self._region = region

    @property
    def correo(self):
        # Devuelve el correo del usuario
        return self._correo

    @correo.setter
    def correo(self, valor):
        # Permite modificar el correo del usuario
        self._correo = valor

    @property
    def edad(self):
        # Devuelve la edad del usuario
        return self._edad

    @edad.setter
    def edad(self, valor):
        # Permite modificar la edad del usuario
        self._edad = valor

    @property
    def region(self):
        # Devuelve la región del usuario
        return self._region

    @region.setter
    def region(self, valor):
        # Permite modificar la región del usuario
        self._region = valor

    def contestar_encuesta(self, encuesta, respuestas):
        """
        Permite al usuario contestar una encuesta.
        Crea un ListadoRespuestas y lo agrega a la encuesta.
        """
        listado = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado)
        return listado
