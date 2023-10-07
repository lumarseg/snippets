# NUMPY-101

Tomado de mis notas del Curso Básico de Manipulación y Transformación de Datos con Pandas y Numpy de Platzi.

NumPy es una librería de Python que proporciona funciones matemáticas avanzadas para trabajar con arrays y matrices de números. Esta librería es muy útil para realizar cálculos numéricos de manera eficiente y rápida.

## ¿Para qué se usa NumPy?

NumPy se utiliza principalmente para realizar cálculos matemáticos y estadísticos en grandes conjuntos de datos. Algunas de las tareas más comunes que se pueden realizar con NumPy son:

- Manipulación de arrays y matrices de números
- Generación de números aleatorios
- Realización de operaciones matemáticas como la multiplicación de matrices o el cálculo de la media de un conjunto de datos
- Integración con otras librerías de ciencia de datos como Pandas y SciPy

## Instalación

Para instalar NumPy, puedes utilizar el administrador de paquetes de Python `pip` o con `conda`:

### Instalación usando pip

```bash
pip install numpy
```

### Instalación usando conda

Para instalar NumPy con Conda, primero debes asegurarte de tener Conda instalado en tu computadora. Si aún no lo tienes instalado, puedes seguir estos pasos:

Descarga e instala Anaconda o Miniconda desde la página oficial de Conda: <https://docs.conda.io/en/latest/miniconda.html>

Abre una terminal y escribe el siguiente comando para actualizar Conda:

```bash
conda update conda
```

Una vez que tienes Conda instalado, puedes instalar NumPy con el siguiente comando:

```bash
conda install numpy
```

Este comando instalará NumPy y cualquier otra librería necesaria de manera automática. Si quieres instalar una versión específica de NumPy, puedes especificarla con el parámetro -n, por ejemplo:

```bash
conda install numpy=1.18.5
```

## Uso básico

Aquí dejo un ejemplo básico de cómo se puede utilizar NumPy para crear y manipular un array:

```python
# Crear un array de 10 elementos con valores consecutivos
a = np.arange(10)
print(a)  
# [0 1 2 3 4 5 6 7 8 9]

# Redimensionar el array a una forma de 2 filas y 5 columnas
a = a.reshape(2, 5)
print(a)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]

# Obtener la suma de todos los elementos del array
print(a.sum())  
# 45

# Obtener la media de todos los elementos del array
print(a.mean())
# 4.5
```
