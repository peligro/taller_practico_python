import platform
import psutil#pip3 install psutil
import multiprocessing
import sys


#número de CPU del sistema
print(f"número de CPU del sistema = { psutil.cpu_count() }")
print(f"número de CPU del sistema = { multiprocessing.cpu_count() }")

#tipo de máquina
print(f"tipo de máquina={platform.machine()}")
print(f"tipo de máquina={platform.architecture()[0]}")

#tipo de software
print(f"tipo de software={platform.python_compiler()}")

# Modelo o liberación del sistema
print(f"Modelo o liberación del sistema={platform.release() }")

#hostname
print(f"hostname={platform.node()}")

#nombre de la red asociada al equipo
print(f"nombre de la red asociada al equipo={platform.node()}")

#Plataforma base del sistema (tipo de kernel)
print(f"Plataforma base del sistema (tipo de kernel)={platform.platform()}")


#tipo de sistema operativo
print(f"tipo de sistema operativo={platform.system()}")
print(f"tipo de sistema operativo={sys.platform}")


#tipo de procesador
print(f"tipo de procesador = {platform.processor()}")

#versión del sistema operativo
print(f"versión de sistema operativo: {platform.version()} ")


#información del sistema
print(f"información del sistema={platform.uname()}")

#versión de python
print(f"versión de python={platform.python_version()}")

#versión de java
print(f"versión de java={platform.java_ver()}")



