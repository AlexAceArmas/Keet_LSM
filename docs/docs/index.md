# Documentación Keet!

## Descripción del proyecto
Según la Organización Mundial de la Salud, más del 5% de la población global
padece alguna discapacidad auditiva y, para 2050, se estima que más de 900 millones
de personas tendrán pérdida auditiva. Particularmente en México, esta condición
afecta a 4.2 millones de personas.
Para abordar esta problemática, se propone una solución innovadora basada en
visión por computadora y aprendizaje profundo para clasificar la Lengua de Señas
Mexicana y expresiones faciales, fundamentales en la comunicación efectiva de esta
comunidad.
En primer lugar,se creó una base de datos con las posiciones extraídas de las manos
y el rostro utilizando redes neuronales convolucionales. La base de datos incluye 200
muestras de 31 señas (estáticas y dinámicas), así como 700 muestras de 4 expresiones
faciales de interés. Con estos datos, se entrenaron redes neuronales y LSTM para el
reconocimiento de señas estáticas, expresiones faciales y señas dinámicas, utilizando
1 y 30 frames, respectivamente. Nuestros modelos alcanzaron precisiones del 95% en
señas estáticas, 93% en expresiones faciales y 88% en señas dinámicas.
Finalmente, dichos modelos se incorporaron a una interfaz de usuario que traduce
las señas y las vocaliza a través de un modelo preentrenado de text-to-speech. Es-
te desarrollo tecnológico promueve la inclusión social y mejora la comunicación en
entornos educativos y sociales para personas con limitaciones auditivas.

## Estructura
    It is code
    It is also code
    It IS ALSO CODE

[This is a link](http://127.0.0.1:8000/getting-started/)

<mark>highlight</mark>

