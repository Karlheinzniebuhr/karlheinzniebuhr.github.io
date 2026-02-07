---
layout: post
title: "Los diferentes tipos de consenso del Blockchain"
date: 2017-05-31 21:50:07 +0000
categories: [Blog]
tags: [Blogging, Crypto, Investing]
---

En un sistema descentralizado como el que usan la mayoría de las criptomonedas se da el problema de la confianza. Como uno puede verificar si todos respetan las reglas si no hay una "autoridad" en el sistema?
Las criptomonedas y otros sistemas distribuidos utilizan una base de datos distribuida que se llama Blockchain para funcionar. El blockchain es literalmente una cadena de bloques, la cual forma el libro de contabilidad del sistema.
Cómo se sabe si alguien ya gastó su dinero por ejemplo? Si un atacante esta en una red distribuida podría tratra de comprar cosas simultaneamente de dos bloques distintos A y B. Si A y B no logran comunicarse a tiempo para avisar que el atacante ya gastó el dinero, los dos aceptarían el pago y habría un dilema. Para evitar eso siempre todos los participantes de la red distribuida tienen que tener una copia del libro de contabilidad con todas las transacciones hechas hasta el momento.
Y para decidir cual libro de contabilidad es el correcto, se tiene que llegar a un consenso. Los algoritmos de consenso que ayudan a que todos los participantes del sistema puedan llegar a un acuerdo para decidir cual bloque representa correctamente las transacciones recientes de la red. Es decir, la confianza en el sistema se produce a través de algoritmos de consenso muy difíciles de engañar.
Hay varios algoritmos para este fin, el mas usado hasta ahora es el Proof-of-Work o PoW (prueba de trabajo).

### Proof-of-Work

Proof-of-Work consiste en problemas matemáticos con dificultad avanzada. De esta forma se requiere de equipos avanzados y un elevado consume de electricidad para resolverlos. De esta manera el sistema se protege contra nodos que tratan de burlar a la red ya que éstos tendrían que resolver una cantidad de problemas tan grande que la posibilidad de que lo hagan se vuelve insignificante.
 
El problema de PoW es el consumo de energía. Los equipos y la electricidad que requieren forman una cantidad abismal de recursos desperdiciados. PoW es prejudicial para el medio ambiente y es una de las razones por la cual yo personalmente empiezo a invertir en sistemas que no utilizan PoW.
Otro problema del costo elevado que implica participar en el trabajo de un sistema PoW es que cada vez menos personas pueden adquirir los equipos necesarios y por lo tanto la comunidad se vuelve mas exclusiva. Esto viola al la idea de la descentralización que justamente busca distribuir al poder, no centralizarlo. La centralización en los sistemas de consenso puede llevar a un [ataque del 51%](http://www.investopedia.com/terms/1/51-attack.asp). El ataque del 51% podría pasar si un nodo controla el 51% del poder de computación que le dejaría hacer todo tipo de trampas como bloquear transacciones o gastar el mismo dinero dos veces. Cómo? Creando y formando sus propios bloques (entradas en el libro de contabilidad) fraudulentos. Los demás simplemente aunque generen bloques (entradas) válidas, simplemente serían invalidados por el agresor.  Es ahí donde PoS realmente podría ayudar. PoS (Proof-of-Stake) es otro tipo de consenso.

#### Proof-of-Stake

En PoS el los participantes sólo pueden contribuir a la computación en la proporción en la cual poseen recursos en el sistema. En el caso de arriba el atacante debería poseer 51% de los bitcoins en existencia, por lo tanto sería poco probable que quiera perjudicar al sistema en el cual posee tantos recursos ya que se percudiría a si mismo debilitando a la moneda. Además sería poco probable que alguien quiera comprar el mayor porcentaje de una moneda por el riesgo de inversión y el precio elevado.
PoS no solo es mas seguro según teoría de juegos, si no que también es mas sustentable y mejor para el medio ambiente. Los cálculos criptográficos en PoS son mucho mas fáciles de computar y por lo tanto no requieren de equipos especializados. Sólo requieren probar que posees cierto porcentaje de monedas en una moneda. El consumo de energía como resultado también es muy leve.
PoS es mas justo y democrático porque invita a participar a cualquiera, no solamente los que pueden adquirir equipos especializados con un costo elevado (más descentralización).
> Nota mental: En PoS la probabilidad de que un participante produzca un bloque válido es proporcional a su recurso en el sistema. En PoW la probabilidad es proporcional al poder de computación del minero.

PoS parece ser el sistema superior, pero aún así tiene algunos problemas. Un problema podría ser que las personas simplemente acumularían monedas para ganarse las comisiones de transacciones, otro problema se conoce como el *nothing-at-stake problem.*Básicamente significa que cuando ocurre un fork, una división de la cadena de bloques, los participantes estarían motivados a participar en ambas ramas, ya que no gastan un precio alto (energía) para hacerlo, como es el caso en PoW. [Este video](https://www.youtube.com/watch?v=pzIl3vmEytY) lo explica en mas detalle. Por suerte la moneda NEM introdujo otro algoritmo que soluciona estos problemas, se llama Proof-of-Importance.

### Proof-of-Importance

Proof-of-Importance es un mecanismo de consenso del blockchain que es muy similar al PoS, pero introduce varias innovaciones nuevas. PoI asigna un puntaje a los participantes basado en su participación en el sistema, en vez de asignarlo sólo en sus recursos (cantidad de monedas). Esto resulta ser un incentivo muy útil ya que previene que los participantes del sistema se dediquen a acumular dinero. En PoI, el que más dinero mueve, más puntos recibe.
> En síntesis, PoI introduce varios mecanismos adicionales para mejorar al PoS.

![](/assets/images/PoI-vs-PoW.png)
