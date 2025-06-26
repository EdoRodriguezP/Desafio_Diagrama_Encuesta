from usuario import Usuario
from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion

# Alternativas para una pregunta
alternativas = [
    {"contenido": "Sí", "ayuda": "Selecciona si estás de acuerdo"},
    {"contenido": "No", "ayuda": "Selecciona si no estás de acuerdo"},
    {"contenido": "Tal vez", "ayuda": ""}
]

# Preguntas para la encuesta
preguntas = [
    {
        "enunciado": "¿Te gusta programar?",
        "ayuda": "Responde sinceramente",
        "requerida": True,
        "alternativas": alternativas
    },
    {
        "enunciado": "¿Has usado Python antes?",
        "ayuda": "",
        "requerida": False,
        "alternativas": alternativas
    }
]

# Crear usuarios
usuario1 = Usuario("ana@mail.com", 25, 1)
usuario2 = Usuario("juan@mail.com", 17, 2)
usuario3 = Usuario("sofia@mail.com", 30, 3)

# Crear encuestas
encuesta = Encuesta("Encuesta General", preguntas)
encuesta_edad = EncuestaLimitadaEdad("Encuesta Adultos", preguntas, edad_min=18, edad_max=99)
encuesta_region = EncuestaLimitadaRegion("Encuesta Región 1 y 3", preguntas, regiones=[1, 3])

# Mostrar encuestas
print(encuesta.mostrar())
print(encuesta_edad.mostrar())
print(encuesta_region.mostrar())

# Usuarios contestan encuestas
print("\n--- Respuestas ---")
usuario1.contestar_encuesta(encuesta, [0, 1])
usuario2.contestar_encuesta(encuesta_edad, [1, 2])  # No se agrega por edad < 18
usuario3.contestar_encuesta(encuesta_edad, [0, 0])  # Sí se agrega
usuario3.contestar_encuesta(encuesta_region, [2, 2])  # Sí se agrega
usuario2.contestar_encuesta(encuesta_region, [1, 1])  # No se agrega, región 2 no permitida

# Verificar respuestas agregadas
print(f"\nRespuestas en 'Encuesta General': {len(encuesta.listados_respuestas)}")
print(f"Respuestas en 'Encuesta Adultos': {len(encuesta_edad.listados_respuestas)}")
print(f"Respuestas en 'Encuesta Región 1 y 3': {len(encuesta_region.listados_respuestas)}")