---
layout: post
title: "Aplicando Deep Learning Style transfer"
date: 2017-06-02 17:06:57 +0000
categories: ["Blog-es"]
tags: ["deep learning", "Machine Learning", "redes neuronales", "computer science", "inteligencia artificial"]
---

En estos días empece con el curso de Deep Learning de Udacity. El primer experimento que hicimos fue transferir estilos de dibujos con Convolutional Neuronal Networks (CNN's) basados en [style-transfer](https://github.com/lengstrom/fast-style-transfer).
Entrare en mas detalle de como funcionan en futuros posts pero in síntesis se trata de entrenar a un modelo de redes neuronales con las obras de un artista. En esencia, las CNN aprenden el estilo del artista y luego pueden aplicar el mismo estilo a cualquier otra imagen.
A continuación algunas de las imágenes que cree con el modelo pre-entrenado con el estilo *Rain Princesss*, del artista [Leonid Afremov](https://afremov.com/Leonid-Afremov-bio.html).

### Esta es la imagen con la cual se entrenó a la red neuronal

![](/assets/images/modelo-1022x1024.jpeg)

### Estas son las imágenes que generó mi CNN con el modelo pre-entrenado

#### Las imágenes originales

![](/assets/images/3-775x1024.jpg) Mi amiga L. alias "Bati"[/caption]
![](/assets/images/2.jpg)

#### Imagenes resultantes al estilo [Leonid Afremov](https://afremov.com/Leonid-Afremov-bio.html)

![](/assets/images/2out.jpg) ![](/assets/images/3out-777x1024.jpg)

### Que tal algo al estilo de Pablo Picasso?

![](/assets/images/3o-777x1024.jpg)
Hay una serie de otros checkpoints (modelos entrenados) que nos facilitaron:

- Rain Princesss, by [Leonid Afremov](https://afremov.com/Leonid-Afremov-bio.html) - [checkpoint](https://d17h27t6h515a5.cloudfront.net/topher/2017/January/587d1865_rain-princess/rain-princess.ckpt)
- La Muse, by [Pablo Picasso](https://en.wikipedia.org/wiki/Pablo_Picasso) - [checkpoint](https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588aa800_la-muse/la-muse.ckpt)
- Udnie by [Francis Picabia](https://en.wikipedia.org/wiki/Francis_Picabia) - [checkpoint](https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588aa846_udnie/udnie.ckpt)
- Scream, by [Edvard Munch](https://en.wikipedia.org/wiki/Edvard_Munch) - [checkpoint](https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588aa883_scream/scream.ckpt)
- The Great Wave off Kanagawa, by [Hokusai](https://en.wikipedia.org/wiki/Hokusai) - [checkpoint](https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588aa89d_wave/wave.ckpt)
- The Shipwreck of the Minotaur, by [J.M.W. Turner](https://en.wikipedia.org/wiki/J._M._W._Turner) - [checkpoint](https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588aa8b6_wreck/wreck.ckpt)

Así que si quieres una imagen con tu estilo favorito, puedes descargarlo de aquí y seguir los pasos del tutorial en Github ;)
Have fun
