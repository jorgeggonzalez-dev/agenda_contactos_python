# Sistema de Gestión y Agenda de Contactos Dinámica 📇📱

Este es un sistema interactivo basado en consola desarrollado en Python que simula una agenda telefónica en tiempo real. El proyecto destaca por el uso eficiente de estructuras de datos bidimensionales (diccionarios) y por la implementación de validaciones rigurosas que garantizan la integridad y persistencia de la información durante la ejecución.

## Características del Proyecto

* **Operaciones CRUD Completas (Create, Read, Update, Delete):**
    * **Lectura Eficiente:** Muestra la lista de contactos ordenados alfabéticamente de forma automática utilizando manipulación de diccionarios con ordenamiento dinámico.
    * **Creación Segura:** Valida en tiempo real que no se registren nombres duplicados dentro de la base de datos local para evitar conflictos de sobreescritura.
    * **Búsqueda Avanzada y Edición:** Permite localizar contactos específicos de manera instantánea y actualizar sus números telefónicos mediante asignación directa de llaves.
    * **Eliminación Controlada:** Remueve registros del diccionario mapeando la clave exacta del usuario de forma segura.
* **Control de Errores y Robustez:**
    * Implementación de bloques `try-except` orientados al manejo de excepciones numéricas (`ValueError`), evitando que el sistema falle si el usuario ingresa letras o caracteres especiales en el campo de teléfono.
    * Control de excepciones de mapeo (`KeyError`) para asegurar que el intento de eliminar un contacto inexistente sea interceptado limpiamente con un mensaje de advertencia en lugar de romper el programa.
* **Interfaz de Consola Estructurada:** Formateo visual limpio mediante el uso de modificadores de texto (`f-strings` con alineación exacta `<10`), simulando una tabla o base de datos visual estandarizada en la terminal.
* **Menú Interactivo Persistente:** Uso estratégico de bucles anidados (`while True`) que permiten al usuario realizar múltiples operaciones de forma consecutiva y regresar al menú principal de manera fluida hasta que decida cerrar sesión voluntariamente.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Estructuras de Datos:** Diccionarios nativos (`dict`) para optimizar el almacenamiento llave-valor y operaciones en tiempo constante $O(1)$.
