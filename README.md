# Gestor de Países

## Trabajo Práctico Integrador - Programación 1

Aplicación desarrollada en Python que permite gestionar información de países a partir de un archivo CSV. El sistema ofrece funcionalidades de búsqueda, filtrado, ordenamiento, actualización y generación de estadísticas mediante una interfaz de consola.

## Integrantes

* Arria Valentina
* Moretto Federico

---

# Objetivos del Proyecto

El objetivo de este trabajo es aplicar los conceptos fundamentales vistos durante la cursada de Programación 1, utilizando:

* Variables y tipos de datos.
* Estructuras condicionales.
* Estructuras repetitivas.
* Funciones.
* Listas.
* Diccionarios.
* Manejo de archivos CSV.
* Manejo de excepciones.
* Modularización del código.

---

# Funcionalidades

## Gestión de Países

* Agregar nuevos países.
* Buscar países por nombre.
* Actualizar población y superficie.
* Persistencia automática en archivo CSV.

## Filtros

* Filtrar por continente.
* Filtrar por rango de población.
* Filtrar por rango de superficie.

## Ordenamientos

* Ordenar por nombre.
* Ordenar por población.
* Ordenar por superficie.
* Orden ascendente y descendente.

## Estadísticas

* País con mayor población.
* País con menor población.
* Diferencia entre ambos.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

---

# Tecnologías Utilizadas

* Python 3
* CSV (Comma Separated Values)
* Programación modular
* Git
* GitHub

---

# Estructura del Proyecto

```text
progr_tp_integrador/
│
├── datos/
│   └── paises.csv
│
├── operaciones/
│   ├── gestion.py
│   ├── filtros.py
│   ├── ordenamientos.py
│   └── estadisticas.py
│
├── utils/
│   ├── csv.py
│   ├── formatting.py
│   ├── input.py
│   ├── menu_handlers.py
│   ├── menus.py
│   ├── prompts.py
│   ├── error_messages.py
│   └── validaciones.py
│
├── main.py
├── README.md
└── tp_integrador_arria_moretto.pdf
```

---

# Dataset Utilizado

El programa trabaja con un archivo CSV con la siguiente estructura:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
Japon,125800000,377975,Asia
Alemania,83149300,357022,Europa
```

---

# Manejo de Errores

El sistema implementa validaciones para:

* Campos vacíos.
* Ingreso de valores no numéricos.
* Poblaciones inválidas.
* Superficies inválidas.
* Países duplicados.
* Búsquedas sin resultados.
* Rangos inválidos en filtros.
* Errores de lectura y escritura del archivo CSV.
* Opciones inválidas en los menús.

---

# Instalación y Ejecución

## Clonar el repositorio

```bash
git clone https://github.com/fedemoretto11/progr_tp_integrador.git
```

## Ingresar al proyecto

```bash
cd progr_tp_integrador
```

## Ejecutar la aplicación

```bash
python main.py
```

---

# Video Demostración

*[TPI progra I.](https://www.youtube.com/watch?v=7qktlNgi2f0)*

---

# Informe

*Ver archivo: tp_integrador_arria_moretto.pdf*

---

# Conclusiones

Este proyecto permitió aplicar los conocimientos adquiridos durante la cursada de Programación 1, integrando estructuras de datos, funciones, validaciones, manejo de archivos CSV y programación modular para desarrollar una aplicación completa de gestión de información.
