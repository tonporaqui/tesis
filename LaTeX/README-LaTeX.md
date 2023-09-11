# Instalación de LaTeX en VSCode en Windows 11

Este documento proporciona una guía paso a paso para instalar y configurar LaTeX en VSCode en un sistema operativo Windows 11.

## Requisitos

- Windows 11
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/)

## Paso 1: Instalar una Distribución de LaTeX

1. Descarga e instala una distribución de LaTeX. Recomendamos [TeX Live](https://tug.org/texlive/) o [MiKTeX](https://miktex.org/).

   - [TeX Live Download](https://tug.org/texlive/acquire-netinstall.html)
   - [MiKTeX Download](https://miktex.org/download)

2. Durante la instalación, asegúrate de añadir la ruta de instalación de LaTeX a tu variable de entorno `PATH`.

## Paso 2: Instalar la Extensión LaTeX Workshop en VSCode

1. Abre VSCode.
2. Ve a la sección de extensiones (puedes usar el atajo `Ctrl+Shift+X`).
3. Busca y instala la extensión [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop).

## Paso 3: Configurar la Extensión LaTeX Workshop

1. Abre la configuración de VSCode (puedes usar el atajo `Ctrl+,`).
2. Busca "LaTeX Workshop" en la barra de búsqueda de configuración.
3. Configura las opciones según tus preferencias. Por ejemplo, puedes configurar la ruta de tu compilador LaTeX, si es necesario.

## Paso 4: Crear y Compilar un Documento LaTeX

1. Crea un nuevo archivo con la extensión `.tex`.
2. Escribe o pega tu código LaTeX en el archivo.
3. Guarda el archivo (puedes usar el atajo `Ctrl+S`).
4. Compila tu documento LaTeX usando la paleta de comandos de VSCode (puedes abrirlo con `Ctrl+Shift+P`) y escribiendo "LaTeX Workshop: Build LaTeX project" y seleccionándolo de la lista.

## Paso 5: Visualizar el Documento PDF

1. Una vez compilado, puedes visualizar el documento PDF resultante directamente en VSCode usando la opción "LaTeX Workshop: View LaTeX PDF".

## Recursos Adicionales

- [LaTeX Workshop Documentation](https://github.com/James-Yu/LaTeX-Workshop/wiki)
- [LaTeX Project](https://www.latex-project.org/)
- Para obtener apoyo visual sobre cómo instalar LaTeX en Windows 11 y cómo configurar VSCode para LaTeX, puedes ver [este video tutorial](https://youtu.be/jIh_gBND02U?si=GAUstFF4Q3beqpW3) que encontré útil.

---

Esperamos que esta guía te haya sido útil para configurar LaTeX en VSCode en Windows 11. ¡Buena suerte con tus proyectos de LaTeX!
