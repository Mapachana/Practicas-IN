# Práctica 1: Análisis predictivo mediante clasificación

> Ana Buendía Ruiz-Azuaga

## Índice

- [Práctica 1: Análisis predictivo mediante clasificación](#práctica-1-análisis-predictivo-mediante-clasificación)
  - [Índice](#índice)
  - [Introducción](#introducción)
  - [Resultados obtenidos](#resultados-obtenidos)
    - [Árboles de decisión (DT)](#árboles-de-decisión-dt)
    - [Random Forest (RF)](#random-forest-rf)
    - [Naive Bayes (NB)](#naive-bayes-nb)
    - [XGBoost (XGB)](#xgboost-xgb)
    - [k-NN (k-NN)](#k-nn-k-nn)
  - [Análisis de resultados](#análisis-de-resultados)
  - [Configuración de algoritmos](#configuración-de-algoritmos)
  - [Procesado de datos](#procesado-de-datos)
  - [Interpretación de resultados](#interpretación-de-resultados)
  - [Contenido adicional](#contenido-adicional)
  - [Bibliografía](#bibliografía)

## Introducción

En esta práctica se trabajará en cuatro problemas de clasificación reales mediante diversos algoritmos de clasificación supervisada implementados en knime, con el objetivo de obtener una predicción y analizar la calidad de esta comparándola con predicciones de otros algoritmos en el mismo problema.

Ahora estudiaremos las particularidades de cada problema por separado:

### Heart 

### Mobile Price

Este problema consiste en intentar predecir a qué rango de precio pertenece un teléfono móvil, donde hay cuatro posibles rangos.

Para ello, se nos proporciona un conjunto de datos con 2000 instancias, de las cuales se nos da información respecto a 20 variables o atributos, y su clase a la que pertencen.

Comenzamos analizando los datos del problema, lo primero en lo que nos fijamos es en que la mayoría ed variables son numéricas, y algunos atributos están marcados con enteros usando 0 o 1 para señalar si un teléfono posee o no una carcaterística, por ejemplo, si es azul o no, o si tiene 4G o no.

Representamos los datos usando una pie chart para comprobar si las clases están balanceadas o no.

> TODO METER FOTO PIE CHART AQUI

Observamos que las 4 clases están igualmente representadas, por lo que el conjunto de datos está balanceado.

Finalmente comprobamos al leer el archivo de datos que el problema no tiene missing values, es decir, no hay ningún atributo que sea desconocido para alguna de las instancias.

Se ha considerado como la clase positiva el rango 0 de precio, aunque se podría haber seleccionado cualquier otro.

### Bank

El objetivo de este problema es realizar predicciones sobre si va a concenderse un crédito en un banco o no basándose en diversos factores.

Para este propósito se nos proporciona un fichero de datos que consta de 41188 instancias, de las cuales conocemos 20 atributos y la clase a la que pertencen, que será sí o no.

Analizamos ahora los datos que nos han proporcionado del problema, al contrario que en el problema de los móviles, aquí podemos observar que hay variables nominales.

Usamos una pie chart para ver a simple vista si los datos están balanceados.

> TODO Meter pie chart

Observamos que los datos están bastante desbalanceados, lo que puede afectar al rendimiento de algunos algoritmos que sean sensibles a ello.

Para terminar el análisis inicial abrimos el archivo de datos y comprobamos que hay missing values, ya que hay atributos que en ocasiones toman un valor "unknown" o "nonexistent", indicando así que son valores desconocidos o perdidos.

Se ha considerado como la clase positiva "yes", ya que queremos predecir cuándo se va a conceder un crédito.

### Tanzania

Este problema consiste en tratar de realizar predicciones sobre qué bombas de agua en Tanzania no funcionan para cambiarlas o repararlas.

Para ello, contamos con un conjunto de datos que consta de 55083 instancias, de las cuales conocemos 39 atributos y la clase a la que pertencen, que podrá tomar valores "funcional" o "no funcional".

Analizamos ahora los datos que nos han proporcionado del problema, de nuevo en este conjunto de datos tenemos atributos nominales a la vez que atributos numéricos.

Usamos una pie chart para ver a simple vista si los datos están balanceados.

> TODO Meter pie chart

Observamos que los datos están bastante desbalanceados, lo que puede afectar al rendimiento de algunos algoritmos que sean sensibles a ello.

Finalmente abrimos el archivo de datos y comprobamos que hay missing values, ya que hay atributos que en ocasiones toman un valor "unknown" o "nonexistent", o en algunos numéricos se ha consdierado el valor "0" como desconocido, indicando así que son valores desconocidos o perdidos.

Se ha considerado como la clase positiva "non functional", ya que queremos predecir cuándo se necesita reparar una bomba de agua.

## Resultados obtenidos

### Árboles de decisión (DT)

> TODO Meter foto DT



### Random Forest (RF)

> TODO Meter foto RF



### Naive Bayes (NB)

> TODO Meter foto NB



### XGBoost (XGB)

> TODO Meter foto XGB



### k-NN (k-NN)

> TODO Meter foto k-NN



## Análisis de resultados



## Configuración de algoritmos



## Procesado de datos



## Interpretación de resultados



## Contenido adicional



## Bibliografía

