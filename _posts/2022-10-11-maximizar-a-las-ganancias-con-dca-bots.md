---
layout: post
title: "Maximizar a las ganancias con DCA bots"
date: 2022-10-11 14:34:20 +0000
categories: [Blog]
tags: [Crypto]
---

Antes de describir a la estrategia en sí, es importante que entendamos bien cómo funcionan los DCA bots. Un DCA bot no trata de predecir al precio, simplemente aprovecha a la volatilidad inherente del mercado.

Veamos un ejemplo de un DCA long bot:

1. Un DCA bot siempre comienzo haciendo una compra (long bot) o venta (short bot), no hace falta un criterio específico para iniciar, simplemente se realiza la compra.

![](/assets/images/Screenshot_1-2-1024x940.png)

2. Si el precio sigue bajando, se realiza una segunda compra, esta vez el monto a comprar puede o no puede ser más grande. Depende de la configuración. Mi configuración favorita es que el monto sea x2 el monto de la primera compra. Nótese que el promedio de compra bajó, y ahora se encuentra entre la primera y segunda compra. Este punto es muy importante.

![](/assets/images/Screenshot_3-1.png)

3. El precio sigue bajando por lo cual el bot realiza una tercera compra, idealmente esta tercera compra sería x3 el monto o el % de la primera. Si la primera compra fue de $10, entonces la tercera sería de $30. Si el bot está configurado para utilizar porcentages -- lo cual recomiendo para que haya compounding automático -- entonces la segunda compra podría ser de 30% del capital vs la primera fue del 10% del capital total. Nuevamente vemos que el promedio de compra se desplaza hacia abajo.

![](/assets/images/Screenshot_4-1.png)

4. Ahora llegó el punto de hacer ganancias, el bot inserta a una orden de venta. Nótese como el precio se encuentra en un punto menor que la compra 1, aún así, salimos haciendo una ganancia. Éste es el superpoder de los DCA bots, pueden hacer ganancias incluso cuando el movimiento del precio va en contra de ellos.

![](/assets/images/Screenshot_5-2-1024x922.png)

---

## Inactividad en los DCA bots

Por supuesto no siempre tiene una oportunidad de vender rápidamente. La ecuación que decide la dimensión de la caída que el bot aguanta sin quedarse inactivo consiste en el capital total del bot y la cantidad de órdenes de compra configuradas así como su tamaño. Veamos un ejemplo para entender mejor.

En la imagen vemos un backtest DCA, las flechas son trades que se ejecutaron. Llegó un punto en donde el bot se quedó sin capital para realizar a más compras y se quedó inactivo. Esto es muy importante de entender. Todos los bots DCA se van a quedar inactivos por periodos de tiempo. Pueden ser días, semanas o incluso meses. Lo contra-intuitivo es que muchas veces los bots que rinden más en el año, también son los que se quedan inactivos por tiempos prolongados. A continuación veremos cómo podemos aprovechar a este patrón.

![](/assets/images/Screenshot_6-1024x616.png)

## Maximizar al compounding DCA

Sabiendo que los DCA bots se quedan parados cuando el mercado baja en exceso, llegamos a la conclusión que en el bear market no queda mucho que hacer para un DCA long bot. La mayoría se quedan suspendidos hasta que el mercado empiece a subir nuevamente. Podemos tomar ventaja de esto haciendo DCA manual.

La mayoría está familiarizada con el concepto de dollar cost averaging. Significa comprar una cantidad definida en intervalos regulares. Por ejemplo, en vez de comprar Ethereum por $12.000 de una sola vez, compras por $1000 cada mes por un año. Qué beneficio trae? Primero nos permite ahorrar progresivamente, si tengo un sueldo, puedo invertirlo mientras lo voy ganando. También da más paz mental ya que no me estreso si el precio baja mucho después de que realizo mi compra. El hecho que haga mis compras progresivamente significa que mi promedio de compra no se ve afectado por las fluctuaciones del mercado.

1+1= ? Ya conectaste los puntos supongo. Qué pasa si combinamos el poder del DCA bot con el poder del DCA manual? Podríamos lograr construir un super DCA long bot en el fondo de un bear market, y aprovechar a toda la subida en el próximo bull market.

![](/assets/images/ETHBTC_2022-10-11_11-59-26-1024x575.png)

En este punto conviene explicar por qué conviene un DCA long en vez de uno short. Los DCA bots sólo funcionan en una dirección es decir tienes que elegir entre una configuración short o una long. Un short bot a largo plazo es más riesgoso ya que a largo plazo el mercado siempre tiende a subir. Entonces la opción más logica es usar un long bot.

También quiero aclarar que usar palanca (leverage) es altamente riesgoso con los DCA bots, y si bien hay páginas como [ésta](https://www.3cstats.com/leverage-bot-calculator/) que permiten calcular los riesgos, yo recomiendo no usar palanca.

## How To

Ahora que aclaramos todo, cómo implementarlo? Yo uso y recomiendo [3commas, es la mejor plataforma bot que conozco y te dan un bot gratis](https://3commas.io/?c=tc389520).

No haré un tutorial completo aquí de como armar a un bot pero encontrarás muchos en YouTube. Lo que debes saber es cómo hacer el **DCA manual**, una vez que tu bot esté corriendo. Para agregar capital manualmente, ingresá en el menú **Trading Bots** y luego **My Deals**. Luego click en el botón **+$ Add Funds**. Listo!

![](/assets/images/Screenshot_7-1024x228.png)

Ya sabes todo para lentamente armar tu super bot y aprovechar al próximo mercado alcista.

## DCA bots vs inversiones

Quiero explicar una duda que capaz tengan, cuál es la diferencia entre un bot y invertir nomás en Ethereum por ejemplo? La diferencia está en el compounding. Supongamos que compras 1 ETH y el precio se duplica, terminas ganando 100% pero sigues teniendo 1 solo ETH. Si haces lo mismo con un DCA long bot, terminarás teniendo 1.5 ETH o algo similar al final del lapso del tiempo. Entonces no sólo ETH vale más, también terminas con más cantidad de ETH.

Los riesgos? Son exactamente los mismos si **NO** usas palanca como recomendé y si **no usas un par que no se va a recuperar** (shitcoin).

Es cierto que los pares de más alto riesgo tienen más volatilidad y por lo tanto puedes ganar más, pero debes tener cuidado con el riesgo de que nunca más alcancen o superen sus puntos máximos. Si insistes en usar pares de riesgo, recomiendo armar un bot diversificado con 10 o más pares. En 3commas encontrarás esas configuraciones hechas o puedes armarlas manualmente.
