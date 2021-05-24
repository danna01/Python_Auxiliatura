# Python_Auxiliatura

**Last update** 18 de mayo de 2021

 * En este repositorio encontrara la informacion correspondiente a la comparacion entre dos simulaciones que se realizaron de cuatro galaxias que estan basadas en los mismos datos y en la misma bibliografia. Por ende, el lector podra encontrar informacion sobre las propiedades de las galaxias calculadas para las dos simulaciones, asi como los resultados y los contrastes obtenidos. Para mayor informacion sobre la informacion en la que se basaron las galaxias remitase a la seccion de bibliografia.

## Ultima modificacion: 19 de Mayo de 2020
**Ultimo avance importante**:Generacion de las animaciones con los valores de los scale length para las galaxias.

## Notebooks

*A continuacion encontrara una lista con los nombres de los notebooks que se han trabajado a lo largo del proyecto con una descripcion sobre
su contenido*

### (1) Test_1
 * En este notebook encontrara la informacion correspondiente a las funciones con las cuales se calcularon los perfiles de densidad de las galaxias y la velocidad maxima de las curvas de rotacion de las mismas. Asi mismo, se encuentran las funciones con las cuales se dio lugar a los plots iniciales con la informacion. Sin embargo, al ser un volumen de informacion tan alto, se recurrio a la generacion de animaciones con los plots generados anteriormente, los cuales tambien se pueden observar en este notebook. Cabe aclarar que la informacion esta dada tanto para las simulaciones de galaxias nuevas como las antiguas. Los productos finales son: Animaciones de perfiles de densidad de gas y de estrellas y la curva de rotacion de gas.

### (2) Test_2
 * En este notebook tenemos nuevamente las funciones que calculan los perfiles de densidad superficial  de gas y de estrellas, junto con la curva de rotacion de gas y su velocidad maxima. Enseguida, con la funcion que genera los plots se crean dos diccionarios (uno para las simulaciones de galaxias nuevas y otro para las simulaciones viejas) en donde se alamacena esta informacion para generar los histogramas de cada una de las propiedades analizadas para cada una de las galaxias.
 * Los productos finales son: Histogramas para cada una de las galaxias de sus propiedades de densidad superficial de gas y de estrellas y para la curva de rotacion del gas.

### (3) Test_3
 * En este notebook puede encontrar la informacion de las simulaciones de galaxias nuevas y viejas correspondiente a la masa de las estrellas, la masa del gas y la masa correspondiente a la materia oscura. Esta informacion esta dada de manera que usted pueda comparar directamente la informacion obtenida en cada simulacion entre si y con la informacion original
 * El producto final es: Tabla donde se resumen las propiedades de masa total de estrella, gas y materia oscura para cada simulacion y para cada galaxia.


## Carpetas

*A continuacion encontrara una lista con los nombres de las carpetas que se han trabajado a lo largo del proyecto con una descripcion sobre
su contenido*   

### (1) Plots
 * En esta carpeta encontrara los plots generados en el Test_1 que corresponde a las propiedades de perfiles de densidad superficial de gas y de estrellas y las curvas de rotacion. Debe existir un plot por cada snapshot.

### (2) Diccionarios
 * Aca encontrara los diccionarios que debera utilizar en caso de que quiera generar nuevamente los histogramas mencionados en el Test_2.

### (3) Animaciones
 * En esta carpeta encontrara las animaciones para cada propiedad generadas en el Test_1. Existe una animacion por cada galaxia, por cada propiedad y por cada simulacion (sea vieja o nueva)

## PDFs

### Jonsson_et_al_2010
 * Este documento corresponde a la bibliografia principal de este proyecto, en donde encontrara los valores iniciales de las galaxias en las cuales fueron basadas las simulaciones que se estan comparando aca. Para comparar los datos aca obtenidos, con los originales puede remitirse a este documento.

## Bibliografia

Jonsson, P., Groves, B. A., & Cox, T. J. (2010). High-resolution panchromatic spectral models of galaxies including photoionization and dust. Monthly Notices of the Royal Astronomical Society, 403(1), 17-44. [Document](https://ui.adsabs.harvard.edu/abs/2010MNRAS.403...17J/abstract) 

### Links de interés

- [Awesome readme files](https://github.com/matiassingers/awesome-readme)
- [Manual de animaciones con matplotlib](https://www.kdnuggets.com/2019/05/animations-with-matplotlib.html)
- [Manual de animaciones con MoviePy](https://splox.net/resources/create-animations-with-moviepy/?fbclid=IwAR3Mvie7GbbPg-t8QKKQCa2UJ9LGDpGCBWDQwo3J_saGXY0NEUt3t_I2B6o)


