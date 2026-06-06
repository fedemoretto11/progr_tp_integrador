# Gestor de Paises en Python

## Descripcion

Este proyecto fue desarrollado para el Trabajo Practico Integrador de la materia Programacion 1 de la Tecnicatura Universitaria en Programacion a Distancia.

El sistema permite gestionar informacion de paises utilizando Python, aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, manejo de archivos CSV, filtros, ordenamientos y estadisticas.

Los datos son cargados desde un archivo CSV y pueden ser consultados y administrados mediante un menu interactivo por consola.

---

## Integrantes

* Federico Moretto
* [Nombre del segundo integrante]

---

## Tecnologias utilizadas

* Python 3.x
* Archivo CSV
* Listas
* Diccionarios
* Funciones
* Manejo de excepciones

---

## Estructura del proyecto

```text
progr_tp_integrador (sujeto a modificaciones)/
│
├── datos/
│   └── paises.csv
│
├── main.py
│
├── README.md
│
└── docs/
    └── informe.pdf
```

---

## Funcionalidades

### Gestion de paises

* Agregar pais.
* Actualizar poblacion y superficie.
* Buscar pais por nombre.

### Filtros

* Filtrar por continente.
* Filtrar por rango de poblacion.
* Filtrar por rango de superficie.

### Ordenamientos

* Ordenar por nombre.
* Ordenar por poblacion.
* Ordenar por superficie.
* Orden ascendente y descendente.

### Estadisticas

* Pais con mayor poblacion.
* Pais con menor poblacion.
* Promedio de poblacion.
* Promedio de superficie.
* Cantidad de paises por continente.

---

---

## Dataset

El programa utiliza un archivo CSV con la siguiente estructura:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
Japon,125800000,377975,Asia
Alemania,83149300,357022,Europa
```

---

## Manejo de errores

El sistema contempla validaciones para:

* Campos vacios.
* Ingreso de valores no numericos.
* Paises duplicados.
* Busquedas sin resultados.
* Errores de lectura del archivo CSV.
* Opciones invalidas de menu.

---

## Video demostracion

Pendiente.

---

## Documentacion

Pendiente.

---

## Conclusiones

Este trabajo permitio aplicar los conceptos fundamentales desarrollados durante la cursada de Programacion 1, especialmente el uso de listas, diccionarios, funciones, manejo de archivos CSV y tratamiento de excepciones para desarrollar una aplicacion modular y reutilizable.
