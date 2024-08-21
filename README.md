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

En la parte imaginaria lo que se hace es que se multiplica a0 con b1 y se le suma el valor de a1 multiplicado b0. Se ve: ((a0 * b1)+ (a1*b0)) 

El final es: ((a0* b0) - (a1*b1) , (a0 * b1)+ (a1*b0))

#División:
