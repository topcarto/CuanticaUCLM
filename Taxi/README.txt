PROBLEMA DE LOS TAXIS // PROBLEMA DE LOS AMIGOS Y LOS ENEMIGOS

ENUNCIADO
El enunciado de este problema es el siguiente: Considérese 3 personas que tienen que ir a un mismo sitio por medio de un taxi. Sólo quedan 2 taxis disponibles,
por lo que al menos uno de los dos taxis tiene que ser compartido por 2 personas. Los taxis son exactamente iguales, por lo que da igual qué taxi se elija.
Sabemos que la persona 1 y la persona 2 son muy amigos entre ellos, y no les importaría compartir el mismo taxi; sin embargo, la persona 3 se lleva mal con los
otros dos. Realiza un programa de computación cuántica que devuelva una posible solución a esta situación.


TRADUCCIÓN
Este problema tiene una traducción muy simple. Ya que solo hay 2 taxis en los que cada una de las 3 personas pueda tomar, podemos hacer que estas personas pasen
a ser variables binarias, y que su valor determine en qué taxi se acaban sentando. Por lo tanto, tenemos 3 variables (a1,a2,a3) que pueden tener 2 estados (taxi 0,
taxi 1).


FORMALIZACIÓN
Este problema encaja perfectamente en el perfil de un BQM (Binary Quadratic Model) al que le vamos a buscar la opción con menos energñia; por lo que para resolverlo
nos ayudaremos de las matrices y de la fórmula:

BQM=min(objetivo+(lambda)(requisitos))

Esta fórmula normalmente tendría una resolución en 2 partes, pero ya que solo tenemos un objetivo, sin ninguna restricción, vamos a centrarnos solo en encontrar el
primer término. Vamos a ir paso a paso para poder sacar esta función, que nos ayudará a construir nuestra tabla.


OBJETIVO
El objetivo se refiere a cuál es el objetivo final del enunciado. Viene a ser lo que vamos a evaluar para decidir qué solución es más válida de todas. Esto en el
mundo de la programación cuántica sería la cantidad de energía que tiene una solución.

El objetivo de esta función es encontrar la solución más óptima para montar a estas personas en los 2 taxis basándonos en sus relaciones personales entre cada uno.
Para hallar la función que encripta este objetivo, primero hay que hacer una tabla para evaluar cada caso posible. Al ser un problema de 3 variables, esto no es
mucho problema en esta situación. Sin embargo, conforme se vaya aumentando el tamaño de este problema, más y más difícil será encontrar esta fórmula. La tabla para
este problema sería:

a1 | a2 | a3 | ¿Válido?
0  | 0  | 0  |   No
0  | 0  | 1  |   Sí
0  | 1  | 0  |   No
0  | 1  | 1  |   No
1  | 0  | 0  |   No
1  | 0  | 1  |   No
1  | 1  | 0  |   Sí
1  | 1  | 1  |   No

Y si transformamos los "Sí" y "No" en valores binarios:

a1 | a2 | a3 | ¿Válido?
0  | 0  | 0  |    0
0  | 0  | 1  |    1
0  | 1  | 0  |    0
0  | 1  | 1  |    0
1  | 0  | 0  |    0
1  | 0  | 1  |    0
1  | 1  | 0  |    1
1  | 1  | 1  |    0

Y si por último cambiamos el signo a los resultados para minimizar la energía, tenemos:
a1 | a2 | a3 | ¿Válido?
0  | 0  | 0  |    0
0  | 0  | 1  |   -1
0  | 1  | 0  |    0
0  | 1  | 1  |    0
1  | 0  | 0  |    0
1  | 0  | 1  |    0
1  | 1  | 0  |   -1
1  | 1  | 1  |    0

Ahora deberemos realizar un sistema de 8 ecuaciones con 8 incógnitas, basándonos en:
(x1 * a1) + (x2 * a2) + (x3 * a3) + (y12 * (a1*a2)) + (y13 * (a1*a3)) + (y23 * (a2*a3)) + (z123 * (a1*a2*a3)) + k
Con esta fórmula general, deberemos sustituir los valores de a1, a2 y a3 con los valores de la tabla yendo línea por línea para generar un sistema de ecuaciones
y conocer el valor de cada incógnita. Para este caso, el sistema de ecuaciones sería:

(x1 * 0) + (x2 * 0) + (x3 * 0) + (y12 * 0) + (y13 * 0) + (y23 * 0) + (z123 * 0) + k = 0
(x1 * 0) + (x2 * 0) + (x3 * 1) + (y12 * 0) + (y13 * 0) + (y23 * 0) + (z123 * 0) + k = -1
(x1 * 0) + (x2 * 1) + (x3 * 0) + (y12 * 0) + (y13 * 0) + (y23 * 0) + (z123 * 0) + k = 0
(x1 * 0) + (x2 * 1) + (x3 * 1) + (y12 * 0) + (y13 * 0) + (y23 * 1) + (z123 * 0) + k = 0
(x1 * 1) + (x2 * 0) + (x3 * 0) + (y12 * 0) + (y13 * 0) + (y23 * 0) + (z123 * 0) + k = 0
(x1 * 1) + (x2 * 0) + (x3 * 1) + (y12 * 0) + (y13 * 1) + (y23 * 0) + (z123 * 0) + k = 0
(x1 * 1) + (x2 * 1) + (x3 * 0) + (y12 * 1) + (y13 * 0) + (y23 * 0) + (z123 * 0) + k = -1
(x1 * 1) + (x2 * 1) + (x3 * 1) + (y12 * 1) + (y13 * 1) + (y23 * 1) + (z123 * 1) + k = 0

Usando la herramienta de WolframAlpha(https://www.wolframalpha.com/) o haciéndola por otros medios, descubrimos que los valores de cada incógnita son:
k = 0
a1 = 0
a2 = 0
a3 = -1
b12 = -1
b13 = 1
b23 = 1
c123 = 0

Ahora, usando estos valores, deberemos rellenar la siguiente matriz triangular, que representa los posibles estados de este problema:
   a1 |a2 |a3 |
a1|x1 |y12|y13|
a2|   |x2 |y23|
a3|   |   |x3 |

Siendo ahora:
   a1 |a2 |a3 |
a1|0  |-1 |1  |
a2|   |0  |1  |
a3|   |   |-1 |
