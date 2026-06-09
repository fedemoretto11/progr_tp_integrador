"""Prompts de usuario y textos de la aplicación - mejora legibilidad."""

# Prompts de búsqueda
PROMPT_BUSCAR_PAIS = "Ingrese el pais a buscar: "

# Prompts de agregar país
PROMPT_AGREGAR_NOMBRE = "\nIngrese el nombre del pais, o 'salir' para abortar el proceso: "
PROMPT_AGREGAR_POBLACION = "\nIngrese la poblacion en habitantes, o 'salir' para abortar el proceso: "
PROMPT_AGREGAR_SUPERFICIE = "\nIngrese la superficie en km2, o 'salir' para abortar el proceso: "
PROMPT_AGREGAR_CONTINENTE = "\nIngrese el continente, o 'salir' para abortar el proceso: "

# Prompts de actualizar país
PROMPT_ACTUALIZAR_SELECCIONAR = "Seleccione el numero del pais a actualizar: "
PROMPT_ACTUALIZAR_POBLACION = "Ingrese la nueva poblacion: "
PROMPT_ACTUALIZAR_SUPERFICIE = "Ingrese la nueva superficie: "
PROMPT_ACTUALIZAR_VALORES = "Ingrese los nuevos valores (o deje en blanco para mantener los actuales):"
PROMPT_CONFIRMAR_ACTUALIZACION = "¿Actualizar? (s/n): "

# Prompts de filtros
PROMPT_FILTRO_CONTINENTE = "Seleccione continente: "
PROMPT_FILTRO_POBLACION_MINIMA = "Ingrese poblacion minima: "
PROMPT_FILTRO_POBLACION_MAXIMA = "Ingrese poblacion maxima: "
PROMPT_FILTRO_SUPERFICIE_MINIMA = "Ingrese superficie minima (km2): "
PROMPT_FILTRO_SUPERFICIE_MAXIMA = "Ingrese superficie maxima (km2): "

# Prompts de ordenamiento
PROMPT_ORDEN_DIRECCION = "Seleccione direccion (1=Ascendente, 2=Descendente): "

# Mensajes de sección/encabezados
MSG_SECTION_AGREGAR_PAIS = "\nAgregar nuevo pais"
MSG_SECTION_ACTUALIZAR_PAIS = "\nActualizar pais"
MSG_SECTION_BUSCAR_PAIS = "\nBuscar pais"

# Mensajes de confirmación y estado
MSG_PAIS_AGREGADO = "Pais agregado correctamente y guardado en CSV"
MSG_PAIS_ACTUALIZADO = "Pais actualizado correctamente y guardado en CSV"
MSG_OPERACION_CANCELADA = "Operacion cancelada"

# Mensajes de advertencia
MSG_ADVERTENCIA_CSV = "Advertencia: No se pudo guardar en CSV: "
MSG_ADVERTENCIA_MEMORIA = "El pais fue agregado en memoria pero no se guardaró permanentemente"
MSG_ADVERTENCIA_ACTUALIZAR = "El pais fue actualizado en memoria pero no se guardaró permanentemente"

# Etiquetas de salida
LABEL_LISTA_PAISES = "--- Lista de Paises ---"
LABEL_PAIS = "Pais:"
LABEL_POBLACION = "Poblacion:"
LABEL_SUPERFICIE = "Superficie:"
LABEL_CONTINENTE = "Continente:"
LABEL_CONTINENTES_DISPONIBLES = "\nContinentes disponibles:"
LABEL_PAISES_ENCONTRADOS = "\nEncontrados varios paises:"
LABEL_SELECCIONAR_PAIS = "Seleccione el numero del pais a actualizar: "
LABEL_PAIS_SELECCIONADO = "\nPais seleccionado: "
LABEL_POBLACION_ACTUAL = "Poblacion actual: "
LABEL_SUPERFICIE_ACTUAL = "Superficie actual: "
LABEL_CONFIRMAR_ACTUALIZACION = "\n¿Confirmar actualización?"
LABEL_POBLACION_CAMBIO = "Población: "
LABEL_POBLACION_ARROW = " → "
LABEL_SUPERFICIE_CAMBIO = "Superficie: "
LABEL_SEPARADOR = "-----------------------------"

# Opciones de selección
OPCION_SI = "s"
OPCION_NO = "n"

# Formatos de salida
FORMAT_PAIS_CON_POBLACION_SUPERFICIE = "{i}. {nombre} (Población: {poblacion}, Superficie: {superficie} km2)"
FORMAT_KM2 = " km2"
FORMAT_CONTADOR = " ({count} paises)"

# Estadísticas
LABEL_MAYOR_POBLACION = "--- Mayor Población ---"
LABEL_MENOR_POBLACION = "--- Menor Población ---"
LABEL_DIFERENCIA = "\nDiferencia: "
LABEL_PROMEDIO_POBLACION = "\nPromedio Población: "
LABEL_PROMEDIO_SUPERFICIE = "\nPromedio Superficie: "
LABEL_CANTIDAD_POR_CONTINENTE = "\nCantidad de Países por Continente:"
LABEL_TOTAL = "\nTotal: "
LABEL_PAISES = " países"

# Menús
LABEL_SECTION_MAIN_MENU = "----- Gestor de Paises -----"
LABEL_OPCION_AGREGAR_PAIS = "Agregar Pais"
LABEL_OPCION_ACTUALIZAR_PAIS = "Actualizar poblacion y superficie"
LABEL_OPCION_BUSCAR_PAIS = "Buscar pais por nombre"
LABEL_OPCION_FILTRAR = "Filtrar paises"
LABEL_OPCION_ORDENAR = "Ordenar Paises"
LABEL_OPCION_ESTADISTICAS = "Mostrar estadisticas"
LABEL_OPCION_MOSTRAR_TODOS = "Mostrar todos los paises"
LABEL_OPCION_SALIR = "Salir"

