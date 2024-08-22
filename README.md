## Proyecto CNYT
#Números complejos

Se realizo un programa con diferentes operaciones de números complejos. Con un total de 9 operaciones en donde cada operación se encarga de 
recibir una o mas tuplas para resolver la operación entre esos números complejos.
Los elementos son:

-Suma

-Resta

-Multiplicación

-División

-Polar a cartesiano

-Cartesiano a polar

-Modulo

-Conjugado

-Fase

#Suma: 

Lo que se hizo en la función de suma, es que se encarga de recibir 2 números complejos en forma de tuplas (a0,a1),(b0,b1).

Luego lo que hace es que toma a0 y b0 de las tuplas y las suma, luego toma a1 y b1 y tambien las suma: 
(a0+b0,a1+b1) donde la suma de a0 y b0 son la parte real y la suma de a1 y b1 son la parte imaginaria.

#Resta: 

Lo que se hizo en la función de restaa, es que se encarga de recibir 2 números complejos en forma de tuplas (a0,a1),(b0,b1).

Luego lo que hace es que toma a0 y b0 de las tuplas y las resta, luego toma a1 y b1 y tambien las resta: 
(a0-b0,a1-b1) donde la resta de a0 y b0 son la parte real y la resta de a1 y b1 son la parte imaginaria.

#Multiplicación: 

Lo que se hizo en la función de multiplicación, es que se encarga de recibir 2 números complejos en forma de tuplas (a0,a1),(b0,b1).

Para la parte real lo que se hizo es que multiplica a0 con b0 y a eso se le resta el valor de la multiplicación de a1 con b1. Se ve: ((a0* b0) - (a1*b1)).

#División:

Se recibe dos tuplas.

Para operar la parte real de la división, se multiplica la parte real de ambas tuplas y a eso se le suma la multiplicación de la parte imaginaria de las tuplas. Al final ese valor se le divide con la suma de los valores de la segunda tupla al cuadrado. Queda: ((a0 * b0)+(a1 * b1) / (a1^2+b1^2))

Para la parte imaginaria se toma el valor real de la seguna dupla, multiplicada con la parte imaginaria de la primera tupla. A ese valor se le resta la multiplicación de la parte imaginaria de la segunda tupla con la parte real de la primera tupla. Y a todo eso se le divide con la suma de los valores de la segunda tupla al cuadrado. Queda: ((b0 * a1)-(b1 * a0) / (a1^2+b1^2))

Al final queda: 

((a0 * b0)+(a1 * b1) / (a1^2+b1^2) , (b0 * a1)-(b1 * a0) / (a1^2+b1^2))

#Polar a cartesiano:

Lo que se hace es que recivimos un tupla en polares y la pasamos a polar. (r,theta). r es la magnitud y theta es el ángulo.

Para la parte real se multiplica r con cos(theta) y la para la parte imaginaria se multiplica r con sen(theta). Regresa una tupla con la parte real y su parte imaginaria.

#Cartesiano a polar: 

Se tiene la tupla con su elemento en x(Real) y su elemento en y(Imaginario).

Para sacar la magnitud se saca la raiz de x^2 + y^2. En el caso del ángulo se saca al arcotangente de y/x. En este caso devuelve una tupla siendo x la magnitud, y es el ángulo.

#Modulo:

En este caso es parecido a sacar la magnitud de un vector.Se tiene la tupla con su elemento en x(Real) y su elemento en y(Imaginario).

Para sacar la magnitud se saca la raiz de x^2 + y^2. En este caso devuele un numero real.

#Conjugado:

En este caso se tiene la tupla con su parte real (x)
y su parte imaginaria (y). Los que se hace es dar una tupla sin afectar la parte real y la parte imaginaria se multiplica con -1 para cambiar su signo.

#Fase:

Se recibe una tupla. Lo que se quiere hacer es sacar el arcotangente de y/x y dar un valor real.
