# Portada

**Inicio de la Investigación**
Mi nombre es Gastón Sepulveda, del Magister en gestión de información & telecomunicaciones, donde presento la defensa de tesis realizada con el título “Análisis de la relación entre la resolución de una guía de programación y éxito académico en el ramo de introducción a la programación”.
Profesor Guía Billy Peralta.

# Planteamiento del Problema

- La programación: En la era digital actual, es esencial en diversos campos de estudio y trabajo.
- La introducción a la programación: es fundamental en programas universitarios, donde se espera que los estudiantes desarrollen habilidades básicas.
- Sin embargo: No se ha estudiado a fondo la relación entre completar una guía y el éxito académico en programación.
- Por lo tanto: Este estudio utiliza herramientas como SHAP y DoWhy para analizar cómo las guías impactan el rendimiento estudiantil.
- Los resultados: ayudarán a mejorar el apoyo a los estudiantes y la decisión sobre el uso de guías como herramienta educativa.

# Justificación

La Justificación de esta investigación es: "Entender cómo la resolución de una guía de programación puede influir en el éxito académico de los estudiantes".

# Objetivo General

Explorar la influencia significativa de la guía de programación en el rendimiento académico de los estudiantes de Introducción a la Programación en la Universidad Andrés Bello, con el propósito de discernir su capacidad predictiva respecto a la deserción estudiantil y formular estrategias de apoyo estudiantil efectivas basadas en los hallazgos.

# Objetivos Específicos

- Recopilación de datos.
- Revisión bibliográfica.
- Análisis descriptivo.
- Validación del modelo.
- Análisis e interpretación de los resultados.
- Conclusiones y recomendaciones.

# Metodología

- Enfoque de la investigación.
- Diseño de la investigación.
- Descripción de la base de datos.
- Comparar Algoritmos.
- Aplicación.
- Análisis e interpretación de resultados.
- Conclusiones y recomendaciones.

# Propuesta de Metodológica

A lo largo de esta investigación se propone una nueva Metodología llamada en sus siglas ACAMD (Análisis Causal Asistido por Minería de Datos)

- Se presenta como una metodología innovadora que integra técnicas avanzadas de minería de datos y análisis causal para proporcionar insights más profundos sobre las relaciones entre variables.
- Se aplicó en este estudio para identificar y analizar las variables clave que influyen en el rendimiento académico de los estudiantes.
- Permite Discusión sobre cómo ACAMD mejora la interpretación de los resultados y proporciona una base más sólida para las decisiones educativas y las estrategias de apoyo estudiantil.

# Descripción de la Base de Datos

- Sol1: indica la calificación obtenida en la primera evaluación.
- Exitosos: indica la cantidad de preguntas respondidas correctamente en la guía.
- Fallidos: indica la cantidad de intentos realizados para resolver preguntas de la guía.
- Hito1 – Hito2: Representa las expectativas de aprendizaje del cruso.
- Columnas de la e0 hasta el e52: siendo las preguntas de la guía.

## Grafico Aprobados y Reprobados

- Intentos Fallidos fue de un 60% e intentos Exitosos fue de un 40%.
- Reprobados de un 54% y Aprobados de un 46%.

# Variable Objetivo

Dado que el objetivo de esta investigación es determinar si la resolución de la guía tiene algún impacto en la aprobación de la prueba de evaluación del curso.

- Sol1 para modelos de regresión.
- Aprobado para modelos de clasificación.

**Introducción a comparación de algoritmos**

En vista que existen varios modelos de regresión y de clasificación, es importante identificar cual modelo nos entregara los mejores resultados.
A continuación, revisaremos los resultados obtenidos bajo esta técnica de comparación de algoritmos.

## Grafico Comparación de Algoritmos Regresión

Podemos observar que los mejores resultados los obtiene el modelo de regresión es “Linear Regresión” con un 14.1% en su R2 más cercano a 1.

## Grafico Comparación de Algoritmos Clasificación

- Podemos observar que los mejores resultados los obtiene el modelo de clasificación “RandomForesClassifier” con un 62.53% en su F1 score siendo la métrica que combina la precisión y el recall en una sola media.

En conclusión, con esta técnica podemos determinar que los datos sobre aprobado el modelo de clasificación RandomForesRegressor es el mas estable y entrega los mejores resultados para realizar una predicción.

# Análisis SHAP

**SHapley Additive exPlanation**
es un enfoque para explicar las predicciones de modelos de aprendizaje automático. SHAP conecta la teoría de juegos con las explicaciones locales, uniendo conceptos de interpretación de modelos y equidad en la contribución de cada característica.

Una vez entrenado el modelo con RandomForesRegressor, revisaremos los resultados obtenidos.

## Características de las variables

Este gráfico proporciona una interpretación doble por medio del eje Y y ejes X:

- Eje Y - Valor de las Características (Feature Value):
  - En el extremo derecho, observamos una distinción cromática donde el rojo denota 'High' indicando variables de alta importancia, mientras que el azul representa 'Low', apuntando a variables de menor relevancia.
  - A la izquierda, se identifican las variables específicas, clasificadas según su importancia relativa.
- Eje X - Impacto en la Predicción:
  - Este eje demuestra cómo la presencia de características específicas incrementa (valores positivos) o disminuye (valores negativos) la predicción del modelo.
  - Los puntos dispersos representan valores individuales de SHAP para cada muestra en el conjunto de datos, reflejando la variabilidad en el impacto que cada característica tiene en las predicciones del modelo, algunos puntos se representan más anchos y separados, estos representan valores atípicos.

Las variables más destacadas incluyen 'Hito1', que exhibe una contribución positiva significativa, indicando su fuerte influencia en la probabilidad de aprobación. Simultáneamente, 'exitosos' y 'fallidos' emergen como importantes, estrechamente vinculadas con la intención del estudiante de interactuar con y completar la guía de estudio.

## Predicción del Modelo

El gráfico muestra la precisión del modelo, resaltando un 81% en su predicción. El 'base value' es el valor promedio de partida para las predicciones, crucial para comparar el efecto de cada variable.

- 'Higher' en rojo señala variables con un impacto positivo significativo en la aprobación.
- 'Lower' en azul indica variables menos influyentes, pero aún relevantes.
- "Base Value" es el valor promedio de las predicciones del modelo sobre todo el conjunto de datos. Es el punto de partida en el gráfico y representa la predicción que haríamos si no tuviéramos información sobre la instancia en particular.
- La marca "f(x)" en el gráfico representa el valor de predicción del modelo. En este caso, el valor es 0.81.

**Introducción a análisis DoWhy**
A continuación, revisaremos la Herramienta DoWhy con el fin de entender las razones fundamentales detrás de los hallazgos obtenidos con SHAP.

# Análisis DoWhy

Los pasos para utilizar esta herramienta son:

- Modelamiento Problema Causal.
- Identificar una estimación objetivo bajo el modelo.
- Estimar el efecto causal con base en la estimación identificada.
- Refutar la estimación obtenida.

## Modelar un problema causal

- En la primera imagen mostramos el primer paso para diagramar el caso causal.
- En la imagen que lo acompaña vemos el modelo causal en formato dot que proporciona la librería.

**Resultados Variables de interés**

- Este grafico esta ordenado por los valores p de la estimación del más significativo al menos significativo.
- Un "valor p" bajo (≤ 0.05) sugiere que los resultados son estadísticamente significativos, mientras que un valor p alto (> 0.05) sugiere que los resultados podrían ser producto del azar.
- El "Valor Medio" indica que, en promedio, un incremento unitario disminuye o aumenta la probabilidad de aprobar.

## Discusión de Resultados con ACAMD

**Comparación DoWhy - SHAP Contribución**

Aunque SHAP Y DoWhy aborden el análisis de las variables desde perspectivas deferentes, es esclarecedor visualizar ambos resultados de manera conjunta para obtener una visión integral.

- Correlaciones:
  Según SHAP, "Hito1" y "e3" fueron variables importantes para la predicción, mientras que DoWhy también muestra efectos causales significativos para estas variables.
- Discrepancias:
  - "e18" muestra una baja significancia en SHAP pero un efecto causal negativo fuerte en DoWhy.
  - La variable "exitosos" es considerada importante en SHAP, pero en DoWhy tiene un "valor p" más alto (0.430) comparado con otras variables como "e3" (valor p: 0.435) o "e18" (valor p: 0.276).
- Discusión de los resultados:
  - e18 “adivina mi número” resulta en clases asistida por el profesor.
  - e42 “los números amigos” tarea para el alumno.
  - e29 “aprobación de créditos” tarea para el alumno.

# Conclusiones

- Contribución Significativa: con la metodología ACAMD, con un enfoque integrado y profundo en su análisis, esta ha revelado insights importantes sobre la influencia de las guías de programación en el rendimiento académico.
- Implicaciones Prácticas: Permite discutir cómo los hallazgos pueden ser utilizados por instituciones educativas para formular estrategias de apoyo estudiantil más efectivas y personalizadas.
- Limitaciones y Futuras Investigaciones: Reconocimiento de las limitaciones del estudio actual y sugerencias sobre cómo las investigaciones futuras podrían abordar estas brechas, posiblemente mediante la incorporación de más variables, el uso de diferentes contextos educativos, o la aplicación de ACAMD en otros campos.
- Conclusión General: Enfatizar que, a pesar de las limitaciones, este estudio marca un paso importante hacia una comprensión más profunda de los factores que contribuyen al éxito académico en cursos de programación, y destaca el potencial de metodologías avanzadas como ACAMD en la investigación educativa.

Gracias.
