"""Mensajes de error centralizados para toda la aplicación."""

# Mensajes de validación general
MSG_NO_PAISES_CARGADOS = "No hay paises cargados"
MSG_OPCION_INVALIDA = "[ERROR]: Opcion invalida"
MSG_SELECCION_INVALIDA = "[ERROR]: Seleccion invalida"

# Mensajes de éxito
MSG_EXITO_PAIS_AGREGADO = "[EXITO]: Pais agregado correctamente y guardado"
MSG_OPERACION_CANCELADA = "OPERACION CANCELADA"

# Mensajes de entrada (input)
MSG_ERROR_ENTERO = "[ERROR]: Debe ingresar un numero entero"
MSG_ERROR_CAMPO_VACIO = "[ERROR]: El campo no puede estar vacio"

# Mensajes de CSV
MSG_ERROR_CSV_NO_ENCONTRADO = "[ERROR]: No se encontro el archivo CSV"
MSG_ERROR_ESCRIBIR_CSV = "[ERROR]: No se puede escribir en {ruta}: archivo no encontrado"
MSG_ERROR_PERMISOS_CSV = "[ERROR]: No tiene permisos de escritura en {ruta}"
MSG_ERROR_CSV_CAMPOS_VACIOS = "[ERROR]: El CSV contiene campos vacios"
MSG_ERROR_CSV_COLUMNAS = "[ERROR]: El CSV no tiene las columnas esperadas"
MSG_ERROR_CSV_DATOS_INVALIDOS = "[ERROR]: El CSV contiene datos invalidos"

# Mensajes de gestión de países
MSG_ERROR_PAIS_EXISTE = "[ERROR]: El pais ya existe"
MSG_ERROR_PAIS_NO_ENCONTRADO = "[ERROR]: No se encontraron paises con ese nombre"
MSG_ERROR_POBLACION_POSITIVA = "[ERROR]: La poblacion debe ser mayor a 0"
MSG_ERROR_SUPERFICIE_POSITIVA = "[ERROR]: La superficie debe ser mayor a 0"

# Mensajes de filtros
MSG_ERROR_PAISES_RANGO_POBLACION = "[ERROR]: No hay paises en el rango {min} - {max}"
MSG_ERROR_RANGO_POBLACION = "[ERROR]: Poblacion minima no puede ser mayor a maxima"
MSG_ERROR_PAISES_RANGO_SUPERFICIE = "[ERROR]: No hay paises en el rango {min} - {max} km2"
MSG_ERROR_RANGO_SUPERFICIE = "[ERROR]: Superficie minima no puede ser mayor a maxima"
MSG_ERROR_PAISES_CONTINENTE = "[ERROR]: No hay paises en {continente}"
MSG_ERROR_POBLACION_MIN_MAX = "[ERROR]: Poblacion minima no puede ser mayor a maxima"
MSG_ERROR_SUPERFICIE_MIN_MAX = "[ERROR]: Superficie minima no puede ser mayor a maxima"

# Mensajes de guardar CSV
MSG_ERROR_GUARDAR_CSV = "[ERROR]: No se pudo guardar en CSV"
MSG_ADVERTENCIA_GUARDAR_CSV = "El pais fue agregado en memoria pero no se guardaró permanentemente"
