# PORTADA

## Análisis de la relación entre la resolución de una guía de programación y el éxito académico en el ramo de introducción a la programación

- **Alumno**: Gastón Ernesto Sepúlveda Espinoza.
- **profesor guía**: Billy Mark Peralta Márquez.
- **Curso**: Magister en Gestión de Información & Telecomunicaciones.

# Planteamiento del Problema

- **La programación**: es una habilidad importante en la era digital actual y se ha convertido en una parte integral de muchos campos de estudio y trabajo.
- **La introducción a la programación**: es un curso fundamental en muchos programas universitarios y se espera que los estudiantes adquieran habilidades básicas de programación.
- **Las guías de programación**: son una herramienta educativa común utilizada en los cursos introductorios de programación para ayudar a los estudiantes a practicar y mejorar sus habilidades de programación.
- **Sin embargo**: la relación entre la finalización de una guía de programación y el éxito académico en un curso introductorio de programación no ha sido ampliamente estudiada.
- **Por lo tanto**: el objetivo de este estudio es investigar la relación entre la finalización de una guía de programación y el éxito académico en un curso introductorio de programación, utilizando el marco unificado SHAP y XAI para analizar y comprender cómo las guías de programación influyen en el rendimiento de los estudiantes.
- **Los resultados**: de este estudio serán de gran utilidad para mejorar las estrategias de apoyo a los estudiantes y la toma de decisiones relacionadas con el uso de las guías de programación como herramienta educativa.

# Justificación

- Entender cómo la resolución de una guía de programación puede influir en el éxito académico de los estudiantes.

# Objetivo General

- Explorar la influencia significativa de la guía de programación en el rendimiento académico de los estudiantes de Introducción a la Programación en la Universidad Andrés Bello, con el propósito de discernir su capacidad predictiva respecto a la deserción estudiantil y formular estrategias de apoyo estudiantil efectivas basadas en los hallazgos.

# Objetivos Específicos

- **Recopilación de datos**:
  - Compilación de datos de estudiantes que participaron en el curso de Introducción a la Programación.
  - Inclusión de información sobre el rendimiento en la guía de programación y la primera evaluación.
- **Revisión bibliográfica**:
  - Análisis de estudios previos sobre la influencia de las guías de programación en el rendimiento académico.
  - Consideración de metodologías de enseñanza y factores psicológicos como la autoeficacia y la motivación.
- **Análisis descriptivo**:
  - Evaluación de la distribución de resultados en la guía de programación y evaluaciones.
  - Identificación de patrones y correlaciones significativas entre variables.
- **Construcción del modelo predictivo**:
  - Uso de técnicas avanzadas de análisis de datos y modelos gráficos.
  - Aplicación de herramientas como SHAP y DoWhy para análisis causal.
- Validación del modelo:
  - Empleo de métodos de validación cruzada estratificada.
  - Ajuste y comparación de diferentes modelos de clasificación.
- **Análisis e interpretación de resultados**:
  - Interpretación de como la resolución de las guías influyen en el éxito académico.
  - Exploración de la causalidad y comprensión de variables importantes.
- **Conclusiones y recomendaciones**:
  - Síntesis de hallazgos clave y su relevancia para estrategias educativas.
  - Sugerencias para investigaciones futuras y mejora de estrategias de apoyo estudiantil.

# Metodología

- **Enfoque de la investigación**: Se utilizará un enfoque de investigación mixto, que combina métodos cuantitativos y cualitativos.
  - Enfoque cuantitativo y cualitativo: Se utilizarán métodos cuantitativos para analizar los datos recopilados y métodos cualitativos para obtener información adicional sobre la experiencia de los estudiantes con la guía de programación.
- **Diseño de investigación**:
  - **Metodología KDD**: Se empleará la metodología KDD (Knowledge Discovery in Databases, descubrimiento de conocimiento en bases de datos) para llevar a cabo el análisis de los datos.
- **Descripción de la base de datos**:
  - Datos de estudiantes que tomaron curso de introducción a la programación en 2021.
  - Información sobre el rendimiento en la guía de programación y la primera evaluación.
- **Comparar algoritmos**:
  - Uso de K-Fold y Stratified K-Fold Cross-Validation para validar la eficacia de los modelos.
  - Comparación de diferentes modelos de clasificación para seleccionar el más adecuado.
- **Aplicación**:
  - Implementación de SHAP y DoWhy para análisis causal y explicaciones interpretables de los modelos predictivos.
- **Análisis e interpretación de resultados**:
  - Evaluación de como la resolución de guías influye en el éxito académico.
  - Identificación de variables clave y comprensión de las relaciones causales.
- **Conclusiones y recomendaciones**:
  - Síntesis de hallazgos clave y su relevancia para estrategias educativas.
  - Propuestas para investigaciones futuras y mejora de estrategias de apoyo estudiantil.

# Metodología ACAMD (Análisis Causal Asistido por Minería de Datos)

- **Definición**: Presentación de ACAMD como una metodología innovadora que integra técnicas avanzadas de minería de datos y análisis causal para proporcionar insights más profundos sobre las relaciones entre variables.
- **Aplicación en la Investigación**: Explicación de cómo ACAMD se aplicó en este estudio para identificar y analizar las variables clave que influyen en el rendimiento académico de los estudiantes.
- **Ventajas de ACAMD**: Discusión sobre cómo ACAMD mejora la interpretación de los resultados y proporciona una base más sólida para las decisiones educativas y las estrategias de apoyo estudiantil.

# Descripción de la base de datos

- Universidad Andrés bello.
- Curso de introducción a la programación.
- Del año 2021.
- Resultados de la primera evaluación o solemne 1.
- Los resultados de las preguntas de la - guía resuelta por los alumnos.
- Con 839 registros.

Tabla de las variables y su descripción.

## Grafica Aprobados y Reprobados

- Reprobados 54% y Aprobados 46%.
- Intentos Fallidos de un 60% e intentos Exitosos de un 40%.

# Variable Objetivo

Dado que el objetivo de esta investigación es determinar si la resolución de la guía tiene algún impacto en la aprobación de la prueba de evaluación del curso, se propone utilizar la variable “sol1” como variable objetivo. Dado que esta variable es de tipo cuantitativa, se sugiere generar una nueva columna llamada aprobado, la cual será del tipo binaria. En esta columna, se representaría con el valor 1 a las notas superiores a 4.0 hasta la nota máxima de7.0, mientras que se asignara el valor 0 a aquellas notas inferiores a las indicadas, representando la condición de reprobado.

# Comparación de algoritmos

Presentación del grafico de un mapa mental para visualizar y organizar la información de como se realizara el proceso de comparación de algoritmos.

## Grafica de resultados Modelos de Clasificación

- Se realiza la selección de características con “aprobado” del tipo binario para los modelos de clasificación.
- Podemos observar que los mejores resultados los obtiene el modelo de clasificación “RandomForesClassifier” con un 62.53% en su F1 score siendo la métrica que combina la precisión y el recall en una sola media.

## Grafica de resultados Modelos de Regresión

- Se realiza la selección de características con “sol1” del tipo cuantitativa para los modelos de regresión.
- Podemos observar que los mejores resultados los obtiene el modelo de clasificación “LienarRegression” con un 14.1% en su R2 siendo el coeficiente de determinación donde 1 indica un ajuste perfecto del modelo, en teste caso es el valor más cercano a 1 entre los modelos revisados.

# Análisis SHAP

## Best Model RandomForestRegressor

- El entrenamiento está formado por nuestra variable objetivo con formato binario llamada “Aprobado” en el eje Y.
- Para el eje X utilizaremos las demás variables incluyendo las preguntas de la guía para revisar su comportamiento.
- Para ello realizaremos un train_test_split para un conjunto de entrenamiento de 80% y un conjunto de prueba de 20%.
- Esto se útil para evaluar el rendimiento del modelo en datos no vistos durante el entrenamiento.
- En la imagen 4 se muestra la configuración que nos entregó el mayor resultado en la frecuencia media de la predicción.
- En la imagen numero 4 encontramos la programación realizada para obtener la predicción en base al fold actual.
- En la imagen 5 vemos el código utilizado para realizar la predicción sobre el modelo utilizando shap explainer sobre X_test.

## Características de las variables

Este gráfico proporciona una interpretación dual a través de sus ejes X y Y:

- **Eje Y - Valor de las Características (Feature Value)**:
  - En el extremo derecho, observamos una distinción cromática donde el rojo denota 'High' indicando variables de alta importancia, mientras que el azul representa 'Low', apuntando a variables de menor relevancia.
  - A la izquierda, se identifican las variables específicas, clasificadas según su importancia relativa.
- **Eje X - Impacto en la Predicción**:
  - Este eje demuestra cómo la presencia de características específicas incrementa (valores positivos) o disminuye (valores negativos) la predicción del modelo.
  - Los puntos dispersos representan valores individuales de SHAP para cada muestra en el conjunto de datos, reflejando la variabilidad en el impacto que cada característica tiene en las predicciones del modelo, algunos puntos se representan mas anchos y separados, estos representan valores atípicos.

Las variables más destacadas incluyen 'Hito1', que exhibe una contribución positiva significativa, indicando su fuerte influencia en la probabilidad de aprobación. Simultáneamente, 'exitosos' y 'fallidos' emergen como importantes, estrechamente vinculadas con la intención del estudiante de interactuar con y completar la guía de estudio.

## Predicción del Modelo

El gráfico muestra la precisión del modelo, resaltando un 81% en su predicción. El 'base value' es el valor promedio de partida para las predicciones, crucial para comparar el efecto de cada variable.

- 'Higher' en rojo señala variables con un impacto positivo significativo en la aprobación.
- 'Lower' en azul indica variables menos influyentes, pero aún relevantes.
- "Base Value" es el valor promedio de las predicciones del modelo sobre todo el conjunto de datos. Es el punto de partida en el gráfico y representa la predicción que haríamos si no tuviéramos información sobre la instancia en particular.
- La marca "f(x)" en el gráfico representa el valor de predicción del modelo. En este caso, el valor es 0.81

## Gráfico Dependencia Variable Objetivo.

En los siguientes gráficos podemos visualizar la dependencia entre las variables Exitosos y Fallidos y la variable objetivo Aprobado.

# Análisis DoWhy

A continuación, revisaremos la Herramienta DoWhy en Python con el fin de entender las razones fundamentales detrás de los hallazgos obtenidos con SHAP.

Los pasos para utilizar esta herramienta son:

- Modelamiento Problema Causal
- Identificar una estimación objetivo bajo el modelo
- Estimar el efecto causal con base en la estimación identificada
- Refutar la estimación obtenida

## Hipótesis Causal

En la siguiente imagen podemos visualizar una propuesta de hipótesis causal, según el conocimiento adquirido a lo largo de nuestra investigación.

## Modelar un problema causal

En la primera imagen mostramos el primer paso para diagramar el caso causal propuesto para ello se establece la variable de tratamiento "hito1", la variable de resultado es "aprobado" y utilizamos un graph model construido según la propuesta presentada en la hipótesis causal. en la imagen que lo acompaña vemos el modelo causal en formato dot que proporciona la librería.

## Tratamiento de la estimación

- En la imagen 2 realizamos el paso 2 para identificar la estimación objetivo bajo el modelo.
- En la imagen 3 realizamos el paso 3 que es estimar el efecto causal usando un método basado en árboles, para ello es importante destacar que en este experimento se utiliza el método backdoor.econml.dml.DML y así mantener el experimento inicial sobre el método RandomForestRegressor y la configuración de los parámetros utilizados en el Análisis SHAP.
- En la imagen 4 vemos el paso 4 que es refutar el estimado obtenido.

## Resultados Variables de interés

- El siguiente grafico muestra los resultados obtenidos para la variable de interés "hito1" y las demás variables de interés obtenidas en el Análisis SHAP sobre aprobado.
- Este grafico esta ordenado por los valores p de la estimación del más significativo al menos significativo.
- Un "valor p" bajo (≤ 0.05) sugiere que los resultados son estadísticamente significativos,
  mientras que un valor p alto (> 0.05) sugiere que los resultados podrían ser producto del azar.
- El "Valor Medio" indica que, en promedio, un incremento unitario disminuye o aumenta la probabilidad de aprobar.

## Comparación DoWhy - SHAP Contribución

Aunque SHAP Y DoWhy aborden el análisis de las variables desde perspectivas deferentes, es esclarecedor visualizar ambos resultados de manera conjunta para obtener una visión integral.

- **Correlaciones**:
  - Según SHAP, "Hito1" y "e3" fueron variables importantes para la predicción, mientras que DoWhy también muestra efectos causales significativos para estas variables.
- **Discrepancias**:
  - "e18" muestra una baja significancia en SHAP pero un efecto causal negativo fuete en DoWhy.
  - La variable "exitosos" es considerada importante en SHAP, pero en DoWhy tiene un "valor p" más alto (0.430) comparado con otras variables como "e3" (valor p: 0.435) o "e18" (valor p: 0.276).

# Conclusiones

- **Contribución Significativa**: Resaltar cómo la metodología ACAMD, con su enfoque integrado y profundo análisis, ha revelado insights importantes sobre la influencia de las guías de programación en el rendimiento académico.
- **Implicaciones Prácticas**: Discusión sobre cómo los hallazgos pueden ser utilizados por instituciones educativas para formular estrategias de apoyo estudiantil más efectivas y personalizadas.
- **Limitaciones y Futuras Investigaciones**: Reconocimiento de las limitaciones del estudio actual y sugerencias sobre cómo las investigaciones futuras podrían abordar estas brechas, posiblemente mediante la incorporación de más variables, el uso de diferentes contextos educativos, o la aplicación de ACAMD en otros campos.
- **Conclusión General**: Enfatizar que, a pesar de las limitaciones, este estudio marca un paso importante hacia una comprensión más profunda de los factores que contribuyen al éxito académico en cursos de programación, y destaca el potencial de metodologías avanzadas como ACAMD en la investigación educativa.
