# Cara a Cara (English)

This is the repository for the Cara a Cara (Face to Face) installation [demo here](https://www.youtube.com/watch?v=jmWU0F__93A). 

This installation was developed by students at [Datalab ITAM](datalabitam.com), with support from NGO's [El Día Después](https://eldiadespues.mx/) and [Data Cívica](https://datacivica.org), and as a part of Rodolfo Ocampo undegraduate thesis from ITAM. The installation was inspired by "Level of Confidence" by Lozano-Hemmer. (https://www.lozano-hemmer.com/level_of_confidence.php) 

Through facual recognition, the installation brings the problem of mass dissapreance closer, by showing installation users a photo of the missing person that most resembles them, along with how many missing persons share their same age, name, and place of birth. This project is an experiment on the use of technology traditionally used for personalization, as a tool to bring users closer to a problem by leveraging the closer relationship they have: the relationship with themselves.

Face to Face works through the following steps.

1. The users steps in a cabin, where there is a camera and a screen. 
2. The user takes a photo of her face and inputs data like name, age and place of birth.
3. A neural networks obtains the most important components of the face and creates a reduced vector representation (embedding).
4. The system compares the user's vector embedding with the missing people face embeddings. 
5. The photo that is closest to the user's vector is picked as the closest one. 
6. The users photo, and the photo of the missing person are put side by side for the user to see. 
7. The user is then shown the number of people who have gone missing that share her name, age and place of birth. 
8. The user is shown more information about what can be done about the problem, and encourage her to participate in political actions to demand solutions. 
9. The user's data is deleted


Students who worked in the installation are Rodolfo Ocampo, Javier Cors, Rodrigo Calderón, Jerónimo Aranda, Fernacisco Velasquez and Jose Javier Villicaña. 

The project requires a Raspberry Pi 4, a monitor and Raspberry Pi 4 camera. 

To replicate this installation, you need to install the dependencies in the manual.txt file, and then clone this repository, and start a flask server by typing this in the terminal:

```
export FLASK_APP=index.py
flask run
```
The project should now open in your browser in localhost.

# Cara a Cara (Español) 

En este repositorio encontrarás el código para replicar Cara a Cara [demo here](https://www.youtube.com/watch?v=jmWU0F__93A). 

Cara a Cara es una instalación desarollada por estudiantes de [Datalab ITAM](datalabitam.com), en colaboración con la organización [El Día Después](https://eldiadespues.mx/) y [Data Cívica](https://datacivica.org), y como parte del proyecto de tesis de Rodolfo Ocampo, inspirada en el proyecto ["Nivel de Confianza" de Rafael Lozano-Hemmer.](https://www.lozano-hemmer.com/level_of_confidence.php) 

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

Para instalar este proyecto, instala las dependencias en el Raspberry Pi, corriendo en la terminal las líneas en el archvo manual.txt de este repositorio y luego los siguiente para iniciar un servidor de flask: 

```
export FLASK_APP=index.py
flask run
```

La aplicación se abrirá en tu navegador.

Los estudiantes que participaron en este proyecto son: Rodolfo Ocampo, Javier Cors, Rodrigo Calderón, Jerónimo Aranda, Fernacisco Velasquez and Jose Javier Villicaña
# Referencias útiles
[Recognize faces on a Raspberry Pi w/ camera](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_on_raspberry_pi.py)

[Run a web service to recognize faces via HTTP (Requires Flask to be installed)](https://github.com/ageitgey/face_recognition/blob/master/examples/web_service_example.py)
