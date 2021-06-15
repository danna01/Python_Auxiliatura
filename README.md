# Python_Auxiliatura

**Contribuidores:** Danna Camila Jaimes y Juan Carlos Basto

**Resumen**

 * En este repositorio encontrara la información correspondiente a la comparación entre dos simulaciones que se realizaron de cuatro galaxias que están basadas en los mismos datos y en la misma bibliografía. Por ende, el lector podrá encontrar información sobre las propiedades de las galaxias calculadas para las dos simulaciones, así como los resultados y los contrastes obtenidos. Para mayor información sobre los documentos en los que se basaron las galaxias remitase a la sección de bibliografía.

## Última modificación: 25 de Mayo de 2020
**Último avance importante**: Generación del test 4 donde se encuentran los cálculos adicionales para la materia oscura.

## Notebooks

*A continuación encontrará una lista con los nombres de los notebooks que se han trabajado a lo largo del proyecto con una descripción sobre
su contenido*

### 1) Test_1
 * En este notebook encontrará la información correspondiente a las funciones con las cuales se calcularon los perfiles de densidad de las galaxias y la velocidad máxima de las curvas de rotación de las mismas. Así mismo, se encuentran las funciones con las cuales se dio lugar a los plots iniciales con la información. Sin embargo, al ser un volumen de información tan alto, se recurrió a la generación de animaciones con los plots anteriores, los cuales también se pueden observar en este notebook. Cabe aclarar que la información está dada tanto para las simulaciones de galaxias nuevas como las antiguas. Los productos finales son: Animaciones de perfiles de densidad de gas y de estrellas y la curva de rotación de gas.

### 2) Test_1_b
 * En este notebook encontrara exactamente la misma información que en el notebook anterior, es decir, en el Test_1 solo que los límites considerados para hacer los cálculos son distintos y están calculados a partir del triple del scale length.

### 3) Test_2
 * En este notebook tenemos nuevamente las funciones que calculan los perfiles de densidad superficial  de gas y de estrellas, junto con la curva de rotación de gas y su velocidad máxima. Enseguida, con la función que genera los plots se crean dos diccionarios (uno para las simulaciones de galaxias nuevas y otro para las simulaciones viejas) en donde se almacena esta información para generar los histogramas de cada una de las propiedades analizadas para cada una de las galaxias.
 * Los productos finales son: Histogramas para cada una de las galaxias de sus propiedades de densidad superficial de gas y de estrellas y para la curva de rotación del gas.

### 4) Test_2_b
 * En este notebook encontrará lo mismo que en el test 2 pero los límites considerados para los plots, las animaciones y los gráficos son distintos, y corresponden a los limites del test 1, por ende, los histogramas son distintos.

### 5) Test_3
 * En este notebook puede encontrar la información de las simulaciones de galaxias nuevas y viejas correspondiente a la masa de las estrellas, la masa del gas y la masa correspondiente a la materia oscura. Esta información está dada de manera que usted pueda comparar directamente la información obtenida en cada simulación entre sí y con la información original.
 * El producto final es: Tabla donde se resumen las propiedades de masa total de estrella, gas y materia oscura para cada simulación y para cada galaxia.

### 6) Test_4
 * En este notebook encontrará la información correspondiente a los cálculos realizados para la materia oscura, es decir, encontrará los cálculos de la masa de la materia oscura y la densidad.
 * El producto final es: Plot con la información de la masa acumulada y plot con la información de la densidad para la materia oscura.

## Carpetas

*A continuación encontrará una lista con los nombres de las carpetas que se han trabajado a lo largo del proyecto con una descripción sobre
su contenido*   

### 1) Plots
 * En esta carpeta encontrará los plots generados en el Test_1 que corresponde a las propiedades de perfiles de densidad superficial de gas y de estrellas y las curvas de rotación. Debe existir un plot por cada snapshot.

### 2) Diccionarios
 * Aca encontrará los diccionarios que deberá utilizar en caso de que quiera generar nuevamente los histogramas mencionados en el Test_2(b).

### 3) Animaciones
 * En esta carpeta encontrará las animaciones en formato GIF para cada propiedad generadas en el Test_1. Existe una animación por cada galaxia, por cada propiedad y por cada simulación (sea vieja o nueva).

### 4) Vídeos
 * En esta carpeta encontrará las mismas animaciones de las propiedades generadas en el Test_1 pero en formato mp4.

### 5) Materia_Oscura

 * En esta carpeta encontrará los plots correspondientes al Test_4 que son de la masa acumulada de materia oscura y de la densidad.

#### 5.1) Comparaciones
 * En esta carpeta encontrará los plots de masa acumulada y de densidad de materia oscura para las galaxias G0 y G1 comparadas para las simulaciones nuevas y antiguas.

## PDFs

### Jonsson_et_al_2010
 * Este documento corresponde a la bibliografía principal de este proyecto, en donde encontrara los valores iniciales de las galaxias en las cuales fueron basadas las simulaciones que se están comparando acá. Para comparar los datos acá obtenidos con los originales puede remitirse a este documento.

### Pineda_et_al_2020
 * Este documento corresponde al PDF del paper que encontrara en la bibliografía con el título de Rotation curve fitting and its fatal attraction to cores in realistically simulated galaxy observations.

## Bibliografía

Jonsson, P., Groves, B. A., & Cox, T. J. (2010). High-resolution panchromatic spectral models of galaxies including photoionization and dust. Monthly Notices of the Royal Astronomical Society, 403(1), 17-44. [Document](https://ui.adsabs.harvard.edu/abs/2010MNRAS.403...17J/abstract) 

Pineda, J., Hayward, C., Springel, V., Mendes-de-Oliveira, C. (2017). Rotation curve fitting and its fatal attraction to cores in realistically simulated galaxy observations. Monthly Notices of the Royal Astronomical Society, 466, 63–87. [Document](https://ui.adsabs.harvard.edu/abs/2017MNRAS.466...63P/abstract)


### Links de interés

- [Awesome readme files](https://github.com/matiassingers/awesome-readme)
	- [Manual de animaciones con matplotlib](https://www.kdnuggets.com/2019/05/animations-with-matplotlib.html)
- [Manual de animaciones con MoviePy](https://splox.net/resources/create-animations-with-moviepy/?fbclid=IwAR3Mvie7GbbPg-t8QKKQCa2UJ9LGDpGCBWDQwo3J_saGXY0NEUt3t_I2B6o)


