---
layout: post
title: "Cuál lenguaje de programación debería aprender?"
date: 2018-10-10 09:03:44 +0000
categories: ["Blog-es"]
tags: ["programacion", "software", "tecnologia", "lenguajes de programacion"]
---

Este es un tema sensible ya que depende mucho de lo que quieras hacer. Cada lenguaje tiene sus trade-offs (pro y contra). Pero en hay algunas pautas muy útiles.

- Un lenguaje de programación debería ser divertido de usar y maximizar a tu productividad.

What? Sólo eso? Si! Opino que es lo que más personas deberían preguntarse antes de seleccionar un lenguaje. Mientras más divertido, más productivo serás. Y mientras más soluciones creas, más te va a motivar. Muchas veces los informáticos nos dejamos guiar por nuestros instintos nerd para aprender los lenguajes más exóticos y rápidos en ejecución. Pero mientras no sea un caso de uso muy específico como drivers, kernels etc, el rendimiento de los lenguajes no es un punto muy importante a la hora de elegirlos por una simple razón.

La gran mayoría de cpu-cycles (tiempo de ejecución en la cpu) que el código de un programador en general se ejecutará, no será crítico en términos de performance. Y para las pequeñas partes que sí lo son, uno puede integrar una librería de alto rendimiento. Para dar un ejemplo mas concreto está el caso de Python.

Python en sí no es un lenguaje rápido. En 95% del tiempo no necesito que sea rápido, necesito que mi tiempo de desarrollo lo sea. Para el 5% de las ocasiones que si necesito que sea más rápido, hay montones de librerías y extensiones que puedo usar. Por ejemplo si quiero que mi servidor web sea rápido, puedo usar un web framework como vibora que rivaliza a frameworks de alto performance escritos en rust y cpp.

![](/assets/images/image.png)

<https://github.com/the-benchmarker/web-frameworks>

Otro ejemplo muy bueno es machine learning. Python es el de facto lenguage de ML, pero ML necesita operaciones de alto rendimiento! No problem porque existen abundancia de librerías como numpy, pandas, skikit-learn que son librerías altamente optimizadas en C, utilizables desde python.

La productividad no solo depende de la sintaxis del lenguaje. Tiene que ver con tantos factores que es muy difícil de cuantificar. Pienso que el tamaño de la comunidad es el factor más grande de todos. Una comunidad grande significa que encontrarás librerías y frameworks para la mayoría de problemas que quieras resolver. Es otra razón por la cual Python es mi lenguaje primario.

Otro tema sumamente importante si vas a construir sistemas grandes es la escalabilidad. Un ejemplo rápido, Javascript no es muy escalable porque no usa tipado estático. Razón por la cual Microsoft cambió JS por Typescript al hacer VSCode. Hablando de VSCode, es un ejemplo muy bueno que un paradigma de programación puede tener un impacto mayor sobre el performance que el hecho que sea compilado o interpretado. La vez pasada abri un txt output de nmap de 350MB en diferentes editores para ver cuales lo abrirían. Notepad++ se colgó, Sublime tomó tanto tiempo que perdí la paciencia y lo cerré. Esos dos Editores están escritos en C++ y C, lenguajes compilados muy rápidos.

Pero VSCode abrió al txt sin problemas en pocos segundos. VSCode está escrito en un lenguaje interpretado, Typescript. Cómo es posible eso? Typescript, que es un superset de Javascript, es concurrente. Significa que es muy rápido para cosas que tienen que ver con IO (input/ouput). Al abrir el txt no se queda colgado todo el programa, la UI sigue utilizable hasta que el editor carga todo el archivo.

> Para resumir, a la hora de elegir un lenguaje tienes que pensar en todas las diferentes ramas de la producción del programador, y los requisitos de performance del projecto.

Dicho lo anterior, hay lenguajes más nuevos que sí me llaman la atención. Por el momento hay un lenguaje que me gustaría dedicar tiempo para aprender, Crystal.

Crystal tiene todo lo que siempre quise en un lenguaje. Una sintaxis elegante basada en Ruby, sin sacrificar al performance. Tradicionalmente siempre hubo un trade-off entre facilidad de uso y velocidad de ejecución. Crystal cambió eso y rompió paradigmas. Ahora croe que crystal tiene una comunidad suficientemente madura como para usarlo como lenguaje en producción.

Además soporta Concurrency lo cual es imprescindible, todos los mayores lenguajes están moviendose más hacia el paradigma concurrente [incluso python](https://docs.python.org/3/library/asyncio.html). La gente de crystal hasta esta implementando paralelismo similar a Go.

No voy a entrar en más detalles sobre todas las razones que hacen explotar al uso de Crystal, si quieres aprender más recomiendo que leas a [este artículo.](https://medium.com/@DuroSoft/why-crystal-is-the-most-promising-programming-language-of-2018-aad669d8344f)
