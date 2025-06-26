# Desafío - Diagrama de Clases

En este desafío validaremos nuestros conocimientos de diagramas de clases con clases, atributos, métodos y relaciones.

---

## Descripción

Trabajas en una consultora a la que se le ha encargado desarrollar un software para crear y contestar encuestas. Debes diagramar y programar las relaciones entre usuarios, encuestas, preguntas, alternativas y respuestas, considerando lo siguiente:

---

### Sobre las Alternativas

- Una alternativa tiene:
  - Un contenido (texto)
  - Una ayuda (texto, opcional)
  - Ambos atributos se pueden consultar y modificar libremente.
- Una alternativa solo puede existir como parte de una pregunta.
- Debe haber un mecanismo para mostrar una alternativa, mostrando su contenido y ayuda (si la posee).

---

### Sobre las Preguntas

- Una pregunta tiene:
  - Un enunciado (texto)
  - Una ayuda (texto, opcional)
  - Una indicación de si es requerida (puede ser requerida o no)
  - Una lista de alternativas
  - Todas estas características se pueden consultar y modificar libremente, excepto las alternativas (solo se pueden consultar).
- Una pregunta solo puede existir como parte de una encuesta.
- Debe haber un mecanismo para mostrar una pregunta, mostrando su enunciado, ayuda (si la posee) y sus alternativas (cada una con su ayuda si la posee).

---

### Sobre las Encuestas

- Una encuesta tiene:
  - Nombre (texto)
  - Un listado de preguntas
  - Un listado de listados de respuestas (inicialmente vacío)
  - Solo el nombre puede consultarse y modificarse libremente.
- Debe contar con un mecanismo para mostrar la encuesta, mostrando el nombre, sus preguntas, sus ayudas y alternativas.
- Debe contar con un mecanismo para agregar un listado de respuestas a su lista de listados de respuestas.
- Tipos específicos de encuestas:
  - **Encuestas limitadas por edad:**  
    - Contienen una edad mínima y máxima (números enteros).
    - El mecanismo para agregar respuestas debe validar que el usuario tenga una edad dentro del rango permitido.
  - **Encuestas limitadas por región:**  
    - Contienen una lista de regiones (números enteros).
    - El mecanismo para agregar respuestas debe validar que el usuario pertenezca a una región permitida.

---

### Sobre los Listados de Respuestas

- Un listado de respuestas está asociado a un usuario que lo generó.
- Tiene una lista de respuestas (números enteros).
- Tanto el usuario como las respuestas solo pueden leerse (no modificarse libremente).
- Un listado de respuestas solo puede existir como parte de una encuesta.

---

### Sobre los Usuarios

- Un usuario tiene:
  - Correo (texto)
  - Edad (número entero)
  - Región (número entero)
  - Todos estos datos requieren reglas para ser modificados, pero por ahora se pueden leer y modificar mediante mecanismos específicos.
- Debe contar con un mecanismo para contestar una encuesta, usando el mecanismo de la encuesta para agregar un listado de respuestas.

---

## Requerimientos

1. **Diagrama de Clases:**  
   Entregar un archivo .png o .pdf con el diagrama de clases que represente lo descrito.  
   Debe incluir:
   - Clases involucradas
   - Atributos (con toda la información pertinente)
   - Operaciones
   - Relaciones entre clases

2. **Clase Alternativa:**  
   En `alternativa.py`, crear la clase Alternativa según el diagrama de clases.

3. **Clase Pregunta:**  
   En `pregunta.py`, crear la clase Pregunta según el diagrama de clases.  
   *Tip: Las alternativas se entregan como una lista de diccionarios.*

4. **Clases de Encuesta:**  
   En `encuesta.py`, crear las clases Encuesta, EncuestaLimitadaEdad y EncuestaLimitadaRegion según el diagrama de clases.  
   *Tip: Las preguntas se entregan como una lista de diccionarios.*

5. **Clase Usuario:**  
   En `usuario.py`, crear la clase Usuario según el diagrama de clases.  
   *Opcional: Implementar lógica de operaciones. Si lo haces, primero crea la clase ListadoRespuestas.*

6. **Clase ListadoRespuestas:**  
   En `listado_respuestas.py`, crear la clase ListadoRespuestas según el diagrama de clases.

---