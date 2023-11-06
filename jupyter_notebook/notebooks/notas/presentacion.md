# Portada

**Inicio de la Investigación**
Hoy, analizaremos cómo las guías de programación pueden influir en el éxito académico de los estudiantes.

Mi nombre es **Gastón Sepulveda**, del Magister en gestión de información & telecomunicaciones. Defendiendo la tesis titulada “Análisis de la relación entre la resolución de una guía de programación y éxito académico en el ramo de introducción a la programación”. Mi Profesor Guía es **Billy Peralta**.

# AGENDA

Procederé a defender mi tesis abordando los siguientes aspectos centrales...

- Planteamiento del Problema y Justificación.
- Objetivo General y Específicos.
- Propuesta de Metodología ACAMD.
- Análisis de Resultados con ACAMD.
- Conclusiones y Recomendaciones.

---

# Planteamiento del Problema y Justificación

En la era digital actual, la programación es esencial en diversos campos. La introducción a la programación es fundamental en programas universitarios, donde se espera que los estudiantes desarrollen habilidades básicas. Sin embargo, la relación entre completar una guía y el éxito académico en programación aún no se ha explorado a fondo. Nuestra investigación busca entender cómo la resolución de una guía de programación puede influir en este éxito académico.

---

# Objetivo General

Explorar la influencia significativa de la guía de programación en el rendimiento académico de los estudiantes de Introducción a la Programación en la Universidad Andrés Bello, con el propósito de discernir su capacidad predictiva respecto a la deserción estudiantil y formular estrategias de apoyo estudiantil efectivas basadas en los hallazgos.

---

# Objetivos Específicos

Desde la recopilación de datos y revisión bibliográfica hasta el análisis y conclusiones, nuestro enfoque ha sido sistemático y detallado. Vamos a discutir cómo cada paso contribuyó a nuestros hallazgos.

---

# Propuesta de Metodológica

Hemos desarrollado una metodología innovadora llamada **ACAMD**, que integra técnicas avanzadas de minería de datos y análisis causal. Esta metodología nos ha permitido identificar y analizar las variables clave que influyen en el rendimiento académico de los estudiantes y ha mejorado la interpretación de nuestros resultados.

---

## Introduccion Análisis de Resultados con ACAMD

A continuación, Revisaremos el Análisis de Resultados con ACAMD.

- Minería de datos.
- Variable Objetivo y Comparación de algoritmos.
- Análisis SHAP.
- Análisis DoWhy.

# Minería de datos

La base de datos es provista por la Universidad Andrés Bello, del curso de introducción a la programación del año 2021, esta contiene los resultados obtenidos de la primera evaluación como también contiene los resultados de las preguntas de la guía del curso resulta por los alumnos y cuenta con 839 registros.

Las variables que aportan en esta investigación son:

- Sol1: indica la calificación obtenida en la primera evaluación.
- Exitosos: indica la cantidad de preguntas respondidas correctamente en la guía.
- Fallidos: indica la cantidad de intentos realizados para resolver preguntas de la guía.
- Hito1 – Hito2: Representa las expectativas de aprendizaje del curso.
- Columnas de la e0 hasta el e52: siendo las preguntas de la guía.

---

## Grafico Aprobados y Reprobados

El siguiente grafico nos muestra los alumnos aprobados y reprobados para la primera evaluación, donde alumnos reprobados fue de un 54% y aprobados de un 46%, también podemos observar que existió un 40% de éxito en resolver las preguntas de la guía y un 60% de intentos fallidos para resolver las preguntas.

---

**Introducción Variable Objetivo y Comparación de Algoritmos**
Con la variedad de modelos de regresión y clasificación disponibles, es crucial identificar el más adecuado. Vamos a discutir cómo llegamos a determinar que el modelo RandomForesRegressor proporciona los mejores resultados para nuestros datos.

# Variable Objetivo

Dado que el objetivo de esta investigación es determinar si la resolución de la guía tiene algún impacto en la aprobación de la prueba de evaluación del curso.

Sol1 es nuestra variable objetivo para modelos de regresión y se crea una nueva variable llamada Aprobado para los modelos de clasificación siendo del tipo binaria.

**Comparación de algoritmos**

A continuación, revisaremos un mapa mental para visualizar y organizar la información de cómo se realizaría el proceso de comparación de algoritmos.
Donde por un lado visualizamos los Modelos de Regresión y Clasificación utilizados en este experimento, se utiliza las tácticas de validación por K-Fold para los modelos de regresión y Stratified K-Fold para modelos clasificación, cada uno de estos K-Fold se le aplica validación cruza para así encontrar el mejor modelo y visual los resultados.

---

## Grafico Comparación de Algoritmos Regresión

En la siguiente gráfica podemos observar que los mejores resultados los obtiene el modelo de regresión 'Linear Regression', con un 14.1% en su coeficiente de determinación R2, siendo este más cercano a 1 en comparación con los otros modelos evaluados. Esto indica que, aunque la varianza explicada por el modelo es relativamente baja, 'Linear Regression' es el que mejor se ajusta a los datos dentro del conjunto de modelos considerados en este análisis.

---

## Grafico Comparación de Algoritmos Clasificación

Por otra parte, podemos observar que los mejores resultados los obtiene el modelo de clasificación “RandomForesClassifier” con un 62.53% en su F1 score siendo la métrica que combina la precisión y el recall en una sola media.

En conclusión, con esta técnica podemos determinar que los datos sobre aprobado el modelo de clasificación RandomForesRegressor es el más estable y entrega los mejores resultados para realizar una predicción.

---

# Análisis SHAP

## Introducción Análisis SHAP

**SHAP**, es una herramienta que hemos utilizado para explicar las predicciones de nuestros modelos de aprendizaje automático. Permítanme mostrarles cómo los resultados de SHAP han enriquecido nuestra comprensión de las variables en juego.

---

## Características de las variables

Shap revela insights clave a través de su gráfico 'Características de las variables', donde el eje Y clasifica las variables por su relevancia, con el rojo y el azul indicando alta y baja importancia, respectivamente. En el eje X, se mide el impacto en la predicción, mostrando el efecto positivo o negativo de cada característica. Los puntos dispersos señalan la variación del impacto de cada variable, con los más anchos destacando los valores atípicos.

Las variables más destacadas incluyen 'Hito1', que exhibe una contribución positiva significativa, indicando su fuerte influencia en la probabilidad de aprobación. Simultáneamente, 'exitosos' y 'fallidos' emergen como importantes, estrechamente vinculadas con la intención del estudiante de interactuar con completar la guía de estudio.

---

## Predicción del Modelo

El gráfico de SHAP evidencia la precisión del modelo, destacando un acertado 81% en la predicción. El valor base o ('base value') sirve como referencia inicial para las predicciones, facilitando la evaluación del impacto de cada variable. Las variables 'Higher' resaltadas en rojo contribuyen positivamente a la predicción de aprobación, mientras que las 'Lower' en azul, aunque menos determinantes, mantienen su relevancia. Esta distribución de variables sugiere que el modelo está alineado con el éxito de aprobar, conforme a los objetivos de la investigación.

---

# Análisis DoWhy

DoWhy nos ha ayudado a entender las razones fundamentales detrás de los hallazgos obtenidos con SHAP. A través de DoWhy, hemos podido modelar, identificar, estimar y refutar nuestras hipótesis causales.

## Planteamiento Hipótesis Causal

Para comprender la relación entre las Preguntas de la Guía de programación y las tasas de aprobación, debemos formular una hipótesis causal. Esta indaga cómo y en qué medida dichas preguntas impactan en la probabilidad de éxito en los exámenes.

---

## Problema Causal Modelado con DoWhy

El gráfico ilustra el Problema Causal Modelado mediante DoWhy en formato DOT, desglosando cómo las preguntas de la guía de programación se correlacionan con los indicadores 'Fallidos', 'Exitosos' y 'Hito 1' en la Predicción del Modelo con SHAP. Este modelo nos permite visualizar la influencia directa de 'Exitosos' y 'Hito 1' en la probabilidad de aprobar. Tras construir y analizar el modelo, podemos proceder a verificar y desafiar nuestras hipótesis causales antes de examinar los resultados finales.

**Resultados Variables de interés**

El siguiente gráfico clasifica las variables de interés según la significancia estadística de su estimación, ordenadas del valor p más bajo al más alto. Un valor p menor o igual a 0.05 indica significancia estadística, implicando que los efectos observados probablemente no se deban al azar. En contraste, un valor p alto sugiere una posible aleatoriedad en los resultados. La 'Estimación del Efecto Causal' revela cómo un cambio unitario en las variables afecta la probabilidad de aprobar. Al correlacionar estos hallazgos con el 'base value' de SHAP, obtenemos una comparativa visual y entendemos mejor cómo cada variable influye en la predicción del modelo.

---

## Discusión de Resultados con ACAMD

**Comparación DoWhy - SHAP Contribución**

El análisis integral de SHAP y DoWhy ofrece una perspectiva completa al contrastar sus enfoques distintos en el análisis de variables. Visualizamos la 'Estimación del Efecto Causal' con barras azules y su correspondiente 'Valor-P' en barras naranjas, junto con las contribuciones SHAP en barras verdes para cada variable.

Al discutir los resultados, notamos:

Correlaciones significativas entre SHAP y DoWhy en variables como 'Hito1' y 'e3', ambas resaltadas por su importancia en la predicción y efectos causales. Discrepancias notables, por ejemplo, 'exitosos' muestra importancia en SHAP pero presenta un 'valor p' elevado en DoWhy, indicando menor significancia estadística comparado con 'e3' y 'e18'. La variable 'e18' revela una contribución menor en SHAP pero un impacto causal negativo relevante en DoWhy.

Para profundizar en los resultados, se consultó a Pablo Schwarzen-Berg (Schwarzenber), quien proporcionó una contextualización valiosa sobre el papel de la guía de programación en el éxito académico. Las discusiones subrayaron la importancia de ejercicios específicos como 'e42' y 'e29' como autoaprendizaje, mientras que 'e18' se beneficia de la instrucción directa del profesor. Estos intercambios enriquecieron la interpretación de los datos, vinculándolos con experiencias educativas concretas.

---

# Conclusiones

En las Conclusiones, este estudio ha marcado un hito al aplicar la metodología ACAMD (Análisis Causal Avanzado de Modelos de Datos), proporcionando una comprensión rica y matizada de cómo las guías de programación afectan el rendimiento académico. Los insights obtenidos son de gran relevancia y ofrecen Implicaciones Prácticas significativas que las instituciones educativas pueden emplear para desarrollar estrategias de apoyo estudiantil más efectivas y adaptadas a las necesidades individuales.

En cuanto a las Recomendaciones, el estudio reconoce Limitaciones, como los sesgos inherentes a los datos utilizados y sugiere la inclusión de más variables para refinar la precisión de las predicciones. Además, subraya la importancia de considerar factores no controlados como las emociones, proponiendo que Futuras Investigaciones deberían incorporar métodos que permitan identificar y medir estos aspectos. La metodología ACAMD también se presenta como una herramienta valiosa para explorar otros ámbitos de estudio.

Como Conclusión General, el estudio enfatiza que, a pesar de las limitaciones presentes, los hallazgos constituyen un avance significativo hacia el entendimiento de los elementos que inciden en el éxito académico en el contexto de la programación. Resalta la importancia y el potencial de las metodologías avanzadas como ACAMD en la investigación educativa, abriendo caminos para futuros trabajos que puedan beneficiar la experiencia de aprendizaje de los estudiantes.

---

# Agradecimientos

Me gustaría agradecer a Billy Peralta y Pablo Schwarzen-Berg por su valioso apoyo y contribuciones a esta investigación.

---

# Final

Gracias por su atención. Estoy listo para responder a sus preguntas.
