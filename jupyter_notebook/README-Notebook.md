# Análisis de Datos con Jupyter y Python

Este proyecto utiliza Jupyter y Python para el análisis de datos. A continuación, se detallan los requisitos y pasos para la instalación de dependencias, incluyendo PyGraphviz.

## Requisitos

- python 3.10.9
- vscode

## Dependencias

### Instalación de Dependencias

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```sh
pip install -r requirements.txt
```

### Desinstalación de Dependencias

Para desinstalar las dependencias, puedes utilizar el siguiente comando:

```sh
pip freeze | xargs pip uninstall -y
```

## Instalación de PyGraphviz en Windows

### Paso 1: Instalar Graphviz

1. Descarga e instala Graphviz desde el [sitio web oficial de Graphviz](https://graphviz.gitlab.io/_pages/Download/Download_windows.html). En este ejemplo, usamos la versión 2.46.0 para Windows 10 (64-bit): `stable_windows_10_cmake_Release_x64_graphviz-install-2.46.0-win64.exe`.
2. Durante la instalación, asegúrate de seleccionar la opción para añadir Graphviz a tu variable de entorno `PATH`.

### Paso 2: Verificar la Instalación de Graphviz

1. Verifica que Graphviz está instalado correctamente ejecutando el siguiente comando en una terminal:

   ```sh
   dot -v
   ```

2. Asegúrate de que los directorios include y lib de Graphviz existen y contienen los archivos necesarios. Las rutas predeterminadas suelen ser:

   ```sh
   C:\Program Files\Graphviz\include
   C:\Program Files\Graphviz\lib
   ```

### Paso 3: Instalar PyGraphviz

1. Abre PowerShell como administrador.

2. Ejecuta el siguiente comando para instalar PyGraphviz, asegurándote de especificar las rutas correctas a los directorios include y lib de tu instalación de Graphviz:
   ```sh
   python -m pip install --use-pep517 `
               --config-setting="--global-option=build_ext" `
               --config-setting="--global-option=""-IC:\Program Files\Graphviz\include""" `
               --config-setting="--global-option=""-LC:\Program Files\Graphviz\lib""" `
               pygraphviz
   ```

### Paso 3: Instalar PyGraphviz

1. Para verificar que PyGraphviz se instaló correctamente, abre una terminal de Python e intenta importar el módulo:

```
import pygraphviz
```

# Visualizacion nootebook

Si necesit visualizar el html de los notebook usar:

- https://nbviewer.org/
