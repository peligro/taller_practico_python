import Pmw #pip3 install Pmw
import platform
import threading
import psutil

import socket
import urllib.request
import socket

#https://github.com/antonioam82/System-Info-Console/blob/master/system_info_console.py

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def public_ip():
    lista = "0123456789."
    ip=""
    dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
    for x in str(dato):
	    if x in lista:
		    ip += x
    return ip


print("--------Datos de la red----------------------")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
#ip equipo
print(f"IP de equipo={s.getsockname()[0]}")
s.close()
#nombre equipo
print(f"nombre equipo={socket.gethostbyname(socket.gethostname())}")
print(f"IP pública={public_ip()}")

print("--------Datos del disco----------------------")
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"Dispositivos: {partition.device} | Puntos de montaje= {partition.mountpoint} | File System={partition.fstype}")
    try:
        particiones_usadas = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print("---")
    print(f" Total Size: {get_size(particiones_usadas.total)} | En Uso: {get_size(particiones_usadas.used)} |  Libre: {get_size(particiones_usadas.free)} | Porcentaje: {particiones_usadas.percent}%")


print("--------Datos de la memoria----------------------")
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)} | Disponible: {get_size(svmem.available)} | Usada: {get_size(svmem.used)} | Porcentaje: {svmem.percent}%")
swap = psutil.swap_memory()#memoria de intercambio
print(f"Total: {get_size(swap.total)} | Libre: {get_size(swap.free)} | Usada: {get_size(swap.used)} | Porcentaje: {swap.percent}%")

print("--------Datos del CPU----------------------")
print(f"Núcleos físicos={str(psutil.cpu_count(logical=False))} | Total núcleos={str(psutil.cpu_count(logical=True))}")
cpufreq = psutil.cpu_freq()
print(f"Máxima Frecuencia: {cpufreq.max:.2f}Mhz | Mínima frecuencia={cpufreq.min:.2f}Mhz | Frecuencia actual={cpufreq.current:.2f}Mhz")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
    print(f"Núcleos {i}: {percentage}%\n")
print(f"Total CPU Usado: {psutil.cpu_percent()}%\n")
