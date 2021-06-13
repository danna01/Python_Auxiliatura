# Python_Auxiliatura

**Contribuidores:** Danna Camila Jaimes y Juan Carlos Basto

**Resumen**

 * En este repositorio encontrara la informacion correspondiente a la comparacion entre dos simulaciones que se realizaron de cuatro galaxias que estan basadas en los mismos datos y en la misma bibliografia. Por ende, el lector podra encontrar informacion sobre las propiedades de las galaxias calculadas para las dos simulaciones, asi como los resultados y los contrastes obtenidos. Para mayor informacion sobre la informacion en la que se basaron las galaxias remitase a la seccion de bibliografia.

## Ultima modificacion: 25 de Mayo de 2020
**Ultimo avance importante**: Generacion del test 4 donde se encuentran los calculos adicionales para la materia oscura.

## Notebooks

*A continuacion encontrara una lista con los nombres de los notebooks que se han trabajado a lo largo del proyecto con una descripcion sobre
su contenido*

### 1) Test_1
 * En este notebook encontrara la informacion correspondiente a las funciones con las cuales se calcularon los perfiles de densidad de las galaxias y la velocidad maxima de las curvas de rotacion de las mismas. Asi mismo, se encuentran las funciones con las cuales se dio lugar a los plots iniciales con la informacion. Sin embargo, al ser un volumen de informacion tan alto, se recurrio a la generacion de animaciones con los plots generados anteriormente, los cuales tambien se pueden observar en este notebook. Cabe aclarar que la informacion esta dada tanto para las simulaciones de galaxias nuevas como las antiguas. Los productos finales son: Animaciones de perfiles de densidad de gas y de estrellas y la curva de rotacion de gas.

### 2) Test_1_b
 * En este notebook encontrara exactamente la misma informacion que en el notebook anterior, es decir, en el Test_1 solo que los limites considerados para hacer los calculos son distintos y estan calculados a partir del triple del scale length.

### 3) Test_2
 * En este notebook tenemos nuevamente las funciones que calculan los perfiles de densidad superficial  de gas y de estrellas, junto con la curva de rotacion de gas y su velocidad maxima. Enseguida, con la funcion que genera los plots se crean dos diccionarios (uno para las simulaciones de galaxias nuevas y otro para las simulaciones viejas) en donde se alamacena esta informacion para generar los histogramas de cada una de las propiedades analizadas para cada una de las galaxias.
 * Los productos finales son: Histogramas para cada una de las galaxias de sus propiedades de densidad superficial de gas y de estrellas y para la curva de rotacion del gas.

### 4) Test_2_b
 * En este notebook encontrara lo mismo que en el test 2 pero los limites considerados para los plots, las animaciones y los graficos son distintos, y corresponden a los limites del test 1, por ende, los histogramas son distintos.

### 5) Test_3
 * En este notebook puede encontrar la informacion de las simulaciones de galaxias nuevas y viejas correspondiente a la masa de las estrellas, la masa del gas y la masa correspondiente a la materia oscura. Esta informacion esta dada de manera que usted pueda comparar directamente la informacion obtenida en cada simulacion entre si y con la informacion original
 * El producto final es: Tabla donde se resumen las propiedades de masa total de estrella, gas y materia oscura para cada simulacion y para cada galaxia.

### 6) Test_4
 * En este notebook encontrara la informacion correspondiente a los calculos realizados para la materia oscura, es decir, encontrara los calculos de la masa de la materia oscura y la densidad.
 * El producto final es: Plot con la informacion de la masa acumulada y plot con la informacion de la densidad para la materia oscura.

## Carpetas

*A continuacion encontrara una lista con los nombres de las carpetas que se han trabajado a lo largo del proyecto con una descripcion sobre
su contenido*   

### 1) Plots
 * En esta carpeta encontrara los plots generados en el Test_1 que corresponde a las propiedades de perfiles de densidad superficial de gas y de estrellas y las curvas de rotacion. Debe existir un plot por cada snapshot.

### 2) Diccionarios
 * Aca encontrara los diccionarios que debera utilizar en caso de que quiera generar nuevamente los histogramas mencionados en el Test_2.

### 3) Animaciones
 * En esta carpeta encontrara las animaciones en formato GIF para cada propiedad generadas en el Test_1. Existe una animacion por cada galaxia, por cada propiedad y por cada simulacion (sea vieja o nueva)

### 4) Videos
 * En esta carpeta encontrara las mismas animaciones de las propiedades generadas en el Test_1 pero en formato mp4.

### 5) Materia_Oscura

 * En esta carpeta encontrara los plots correspondientes al Test_4 que son de la masa acumulada de materia oscura y de la densidad.

#### 5.1) Comparaciones
 * En esta carpeta encontrara los plots de masa acumulada y de densidad de materia oscura para las galaxias G0 y G1 comparadas para las simulaciones nuevas y antiguas.

## PDFs

### Jonsson_et_al_2010
 * Este documento corresponde a la bibliografia principal de este proyecto, en donde encontrara los valores iniciales de las galaxias en las cuales fueron basadas las simulaciones que se estan comparando aca. Para comparar los datos aca obtenidos, con los originales puede remitirse a este documento.

### Pineda_et_al_2020
 * Este documento corresponde al PDF del paper que encontrara en la bibliografia con el titulo de Rotation curve fitting and its fatal attraction to cores in realistically simulated galaxy observations.

## Bibliografia

Jonsson, P., Groves, B. A., & Cox, T. J. (2010). High-resolution panchromatic spectral models of galaxies including photoionization and dust. Monthly Notices of the Royal Astronomical Society, 403(1), 17-44. [Document](https://ui.adsabs.harvard.edu/abs/2010MNRAS.403...17J/abstract) 

Pineda, J., Hayward, C., Springel, V., Mendes-de-Oliveira, C. (2017). Rotation curve fitting and its fatal attraction to cores in realistically simulated galaxy observations. Monthly Notices of the Royal Astronomical Society, 466, 63–87. [Document](https://watermark.silverchair.com/stw3004.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAqEwggKdBgkqhkiG9w0BBwagggKOMIICigIBADCCAoMGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMH-Y9-UTvkA2mGdRJAgEQgIICVAjpsrVqYoGYO8pcdIQXpxCAZ6OaiIo_dyQDPqWdxyvWBkNIwnqcQfFg7IUgRnh4j05ffNzvywTQ6YWWB35vsSXjifWgS2hhz4OmdCK67RAVZBorxuTb0UKT7JGLZXv4RPZ9jroEFUYrP7Mk8JoOy4ksT7JvpiE4xJFbcLfXBshalLQYrFjnaweYE1ajBKoiM7FIiVmHHolhUHqp5O14DGzhfDhSWQSqw23LIVA-yEqd5u7TXVnTL69oww-NUyppUmMJ15kWEYlybNs5TJc-UoxcPzMs8NaVhkjYQ9-W8DLRzBsK2CnqGqPmFm3Wx3QTyGQLKmSnVm05LXH7-BQgJF7qdDLbSdPD0XK7VdP9NrK_Qlf8JXq7-onPSKbDwHqO5cRW-zqzRn5MNJd-fxwp6kDUJDfkccyx8BmMypXstw1Qn5WERp0QKMYya3siqteYXoU8E7egiutCf7nM7vKZr635Cuwu8Hh7w_gX2mTgmgjDw3C5gZg5ldwBG8TfE7z9kwfxLtyZCw8uPh-ot7FFFG4SPjN5V6G_B4zrT6Wm5Xn0skhOn2z8GKAHT1gu0rWHKyV4b9MleytMg8qpbCUBlFzVckNfy1TCmBu2QUOdt4tnvKVhxVBGQUJYoNsYqWacy-FdK8lt_kOPjgqe_sXkGNbg31zCUS4iCLPMtL-XGso8Eqg1YpifPA2iqcoRS70wSU40XRo_ndTuSH6eG7dzCTr0cEsGbp2pGMYSJ27DWJDKU6d9sMU5u__qDv8kw7t9Ru2UpH4ZKqf9M71Y3MEKInMAtyEc)


### Links de interés

- [Awesome readme files](https://github.com/matiassingers/awesome-readme)
	- [Manual de animaciones con matplotlib](https://www.kdnuggets.com/2019/05/animations-with-matplotlib.html)
- [Manual de animaciones con MoviePy](https://splox.net/resources/create-animations-with-moviepy/?fbclid=IwAR3Mvie7GbbPg-t8QKKQCa2UJ9LGDpGCBWDQwo3J_saGXY0NEUt3t_I2B6o)


