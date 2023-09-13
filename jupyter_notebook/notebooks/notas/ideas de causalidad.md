segun mi analisis shap partiendo de high con hito1 y low con e8

# Mostrar Grafico de Caracteristicas

shap.summary_plot(shap_values, X_test)
me dice que:
hito1,e29,exitosos,fallidos,e42,e3,e35,e13,e26,e18,e32,e10,e0,e4,e23,e7,e17,e25,e22,e8
son las feature value mas relevantes para aprobar
con respecto a la prediccion realizada por shap con un 81% en su f(x) es:

# Crear la figura de matplotlib

shap.force_plot(
explainer.expected_value, shap_values[0, :], X_test.iloc[0, :], matplotlib=True
)
los valores higher son del mas cercano al 81%
hito1,exitosos,e42,e29,e35,e3,fallidos
y en lower solo me entrega e18

dejando fuera hito2 y el resto de las columnas.

esta es la estrucutra de mi dataframe:
['hito1', 'hito2', 'exitosos', 'fallidos', 'e0', 'e1', 'e2', 'e3', 'e4',
'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15',
'e16', 'e17', 'e18', 'e19', 'e20', 'e21', 'e22', 'e23', 'e24', 'e25',
'e26', 'e27', 'e28', 'e29', 'e30', 'e31', 'e32', 'e33', 'e34', 'e35',
'e36', 'e37', 'e38', 'e39', 'e40', 'e41', 'e42', 'e43', 'e44', 'e45',
'e46', 'e47', 'e48', 'e49', 'e50', 'e51', 'e52', 'sol1', 'aprobado']

donde:
sol1: Nota en la primera evaluación (rango 0.0-7.7)
exitosos: Cantidad de respuestas correctas en la guía
fallidos: Número de intentos en la guía
hito1 hito2: Expectativas de aprendizaje del curso (conjunto de preguntas)
programa: Programa académico del estudiante  
Columnas e0 hasta la e52 & Resultados de la guía (1: correcto, 0: incorrecto)
finalmente se propuso crear la clumna aprobado es la representacion de sol1 donde aprobado es 1 cuando la nota es igual o superior a 4.0.

del analisis shap proporcionado y el ultimo modelo causal
como puedo asegurar un backdoor, frontdoor y iv?
