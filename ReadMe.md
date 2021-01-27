# Cara a Cara

En este repositorio encontrarás el código para replicar Cara a Cara. 

Cara a Cara es una instalación desarollada por estudiantes de [Datalab ITAM](datalabitam.com), en colaboración con la organización [El Día Después](https://eldiadespues.mx/) y [Data Cívica](https://datacivica.org), y como parte del proyecto de tesis de Rodolfo Ocampo, inspirada en el proyecto "Nivel de Confianza" de Rafael Lozano-Hemmer. 

A través de reconocimiento facial, la instalación acerca a los asistentes al problema de la desaparición en México, mostrándo la cara del desaparecide más similar a les usuaries de la instalación. La instalación muestra también estadísticas respecto al número de desaparecides que comparten su misma edad, nombre, apellido, y lugar de nacimiento. El proyecto es un experimento en la utilización de tecnológia normalmente usada para proveer servicios personalizados, como una herramienta para fomente empatía y acción política. 

Cara a Cara funciona de la siguiente manera:

1. El usuarie entra a una cabina, donde se coloca frente a una cámara y pantalla y 
2. El usuarie captura una foto de su cara e ingresa datos como nombre, edad y lugar de nacimiento
2. A partir de la foto, una red neuronal obtiene las características más importantes de la cara de la persona, obteniendo un vector representativo
3. El vector es comparado con una base de datos de las fotos de desaparecides (es decir, con los vectores representativos de las mismas)
4. La foto con una distancia vectorial más cercana es seleccionado como la persona más parecida
5. Se obtienen los datos de la persona desaparecida
6. Se coloca la foto del usuarie y sus datos, junto con la foto y los datos de la persona desaparecida
7. Se muestra al usuarie un resumen sobre cuantas personas en la base de datos comparten su mismo nombre, edad o lugar de nacimiento
8. Se invite al usuario a ejercer presión política para mejorar los sistemas de búsqueda y registro de desaparecides
9. Se borran los datos del usuarie

En términos de hardware, el proyecto require de una Raspberry Pi, una pantalla y un teclado. 

Para instalar las dependencias en el Raspberry Pi, corre en la terminal del RPi las líneas en el archvo manual.txt de este repositorio.

# Referencias útiles
[Recognize faces on a Raspberry Pi w/ camera](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_on_raspberry_pi.py)

[Run a web service to recognize faces via HTTP (Requires Flask to be installed)](https://github.com/ageitgey/face_recognition/blob/master/examples/web_service_example.py)
