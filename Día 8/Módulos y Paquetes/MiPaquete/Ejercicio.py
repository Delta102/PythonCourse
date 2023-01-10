## Llamado a mi paquete
from PaqueteMain import SumaResta
## Llamado a Subpaquete
from PaqueteMain.SubPaquete import Saludo

## PAQUETE
SumaResta.resta(15, 2)
SumaResta.suma(20,55)

## SUBPAQUETE
Saludo.hola()