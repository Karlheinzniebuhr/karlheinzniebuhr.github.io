---
layout: post
title: "Hackatón - Datatón 2020"
date: 2020-09-29 10:22:00 +0000
categories: [Blog, Technology]
---

En la semana pasada se hizo el primer (según mi conocimiento) evento de datos abiertos en Paraguay. El evento consistió en varias charlas a las que por razones no pude asistir. En donde si participé fue en el hackatón. Quiero compartir brevemente mi experiencia en el hackatón.

El viernes 25 a la noche empezó oficialmente el hackatón. Primero llenamos un formulario eligiendo temas de interés. Luego se nos asignó un grupo. También era posible anotarse con personas específicas en un grupo de antemano pero en mi caso, me inscribí solo. A mi me tocó el grupo del Congreso.

Me re alegré cuando alguien compartió este excelente writeup sobre periodismo de datos de Lía Barrios. Es un resumen muy conciso de algunas de las mejores herramientas para limpiar y analizar datos.

[periodismo-de-datos](https://www.karlbooklover.com/wp-content/uploads/2020/09/periodismo-de-datos.pdf)[Download](https://www.karlbooklover.com/wp-content/uploads/2020/09/periodismo-de-datos.pdf)

Últimamente estoy integrando cada vez mas al cloud en mis workflows, pero Google Cloud Dataprep fue algo nuevo para mi. Por supuesto lo probé enseguida y quedé encantado. Es tan potente como Power Query de PowerBI.

![Captura de pantalla de Power BI Desktop en la que se muestra el panel Configuración de la consulta del Editor de Power Query.](/assets/images/queryoverview_withdataconnection.png)

Herramientas como Dataprep o PowerQuery facilitan procesos complejos de limpieza mediante una interface gráfica que permite visualizar en tiempo real los cambios que se van haciendo. En el caso de PowerBI, en la imagen de arriba se ve como a la derecha en la ventana Applied Steps aparecen los cambios que uno va realizando.

![](/assets/images/Screenshot_2020-09-29-Parlamentarios-Transformer-Cloud-Dataprep-1024x426.png)

De forma similar, en Dataprep se ve una tabla con los datos. Puedo crear diferentes cambios en cada columna y esos cambios van apareciendo de forma secuencial a la derecha.

## Procedimiento

Luego de que nos asignaron nuestro grupo, creé una carpeta en Google Drive para empezar la colaboración. Para empezar un análisis de datos suele ser útil formar algunas preguntas interesantes. Eso fue lo que hicimos en un documento, armamos un debate, compartimos ideas y links de interés.

![](/assets/images/imagen-929x1024.png)

No tardaron en llegar los aportes.

Yo me enfoqué en este sitio <http://datos.congreso.gov.py/opendata/datos> porque contiene una lista de datasets descargables en mi formato favorito, csv. Una vez descargado, suelo usar RStudio, Tableau, Data Studio o PowerBI para empezar a jugar con los datos para tener una mejor idea de lo que se puede hacer con los mismos.

Terminé robando la idea de crear un gráfico de Treemap, que resulta muy bien para visualizar el conteo de los periodos de cada parlamentario.

![](/assets/images/Conteo-de-Periodos-por-Parlamentario-1024x616.png)

Para poder realizar el conteo de los nombres, primero convertí todo a mayúsculas y luego eliminé los acentos con ayuda de un poquito de magia en R.

![](/assets/images/imagen-1-1024x208.png)

Fue una gran experiencia y los organizadores así como el equipo fue de alta calidad y buena onda. Espero que este sólo sea el comienzo de una cultura de datos con gran potencial de mejorar a nuestro país.
