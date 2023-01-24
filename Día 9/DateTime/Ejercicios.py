## 1
from datetime import date
mi_fecha = date(1999, 2, 3)


## 2
    # Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada.
from datetime import date
hoy = date.today()
print(hoy)


## 3
    # En una variable llamada minutos, almacena únicamente los minutos de la hora actual.

    # Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43

from datetime import datetime

tiempo = datetime.today()
minutos = tiempo.minute