## 1

    # Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

    # Recuerda importar Path del módulo pathlib, y utilizar el método home()

from pathlib import Path

ruta_base = Path(Path.home())


## 2
    # Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
    # Almacena el directorio obtenido en la variable ruta. No olvides importar Path.

ruta = Path("Curso Python", "Día 6", "practicas_path.py")

## 3

    # Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

rutaBase = Path(Path.home())

ruta = Path(rutaBase, "Curso Python", "Día 6", "practicas_path.py")