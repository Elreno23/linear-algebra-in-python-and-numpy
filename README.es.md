<!-- hide -->
# Álgebra Lineal en Python y NumPy
<!-- endhide -->

En este tutorial, aprenderás a **manipular vectores y matrices en Python** utilizando tanto **listas anidadas** como **arrays de NumPy**. Exploraremos desde operaciones básicas hasta algunas más avanzadas. Para que comprendas bien ambas formas de trabajar con datos en Python, dividiremos el proyecto en dos partes:  

- **Python puro**: Usaremos listas anidadas para representar y operar con vectores y matrices.  
- **NumPy**: Aprenderás a trabajar con arrays, lo que facilita muchas operaciones y optimiza el rendimiento.  

Al final de este tutorial, serás capaz de realizar cálculos con vectores y matrices en Python de manera eficiente y comprenderás cuándo es mejor usar cada enfoque.  



<!-- hide -->

## ✅ Instalación en un clic (recomendado)

Puedes empezar estos ejercicios en pocos segundos haciendo clic en: [Abrir en Codespaces](https://codespaces.new/?repo=4GeeksAcademy/linear-algebra-in-python-and-numpy) (recomendado) o [Abrir en Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/linear-algebra-in-python-and-numpy).

> Una vez ya tengas abierto VSCode, los ejercicios de LearnPack deberían empezar automáticamente, si esto no sucede puedes intentar empezar los ejercicios escribiendo este comando en tu terminal: `$ learnpack start`

## 🖥️ Instalación local:

1. Asegúrate de instalar [LearnPack](https://learnpack.co), node.js version 22.14.0 y Python version 3+. Este es el comando para instalar LearnPack:

```bash
$ npm i @learnpack/learnpack@2.1.20 -g && learnpack plugins:install @learnpack/python@1.0.0
```

2. Clona o descarga este repositorio en tu ambiente local.

```bash
$ git clone https://github.com/4GeeksAcademy/linear-algebra-in-python-and-numpy.git
$ cd linear-algebra-in-python-and-numpy
```

> Nota: Una vez que termine de descargar, encontrarás la carpeta "exercises" que contiene todos los ejercicios.

3. Inicializa el tutorial ejecutando el siguiente comando al mismo nivel en el que se encuentra tu archivo learn.json: 

```bash
$ pip3 install pytest==6.2.5 pytest-testdox mock
$ learnpack start
```

<!-- endhide -->


## ¿Cómo están organizados los ejercicios?

Cada ejercicio es una pequeña aplicación de Python que contiene los siguientes archivos:

1. **app.py:** representa el archivo de entrada de Python que será ejecutado por el computador.
2. **README.es.md:** Contiene las instrucciones del ejercicio.
3. **test.py:** Contiene el script del test para el ejercicio (no es necesario que abras este archivo).

> Nota: Estos ejercicios tienen calificación automática. Los tests son muy rígidos y estrictos, mi recomendación es que no prestes demasiada atención a los tests y los uses solo como una sugerencia o podrías frustrarte.

## Colaboradores

Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors). ¡Todas las contribuciones son bienvenidas!

Este y otros ejercicios son usados para [aprender a programar](https://4geeksacademy.com/es/aprender-a-programar/aprender-a-programar-desde-cero) por parte de los alumnos de 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) realizado por [Alejandro Sánchez](https://x.com/alesanchezr) y muchos otros contribuyentes. Conoce más sobre nuestros [Cursos de Programación](https://4geeksacademy.com/es/curso-de-programacion-desde-cero?lang=es) para convertirte en [Full Stack Developer](https://4geeksacademy.com/es/coding-bootcamps/desarrollador-full-stack/?lang=es), o nuestro [Data Science Bootcamp](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning).
