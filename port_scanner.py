"""
Objetivo del programa: Verificar qué puertos están abiertos en una máquina.

¿De qué sirve saber qué puertos están abiertos?
Saber qué puertos están abiertos en una máquina es útil para:

Seguridad: Identificar posibles vulnerabilidades, ya que los puertos abiertos pueden ser puntos de entrada para ataques.
Administración de red: Verificar qué servicios están activos y funcionando correctamente.
Solución de problemas: Diagnosticar problemas de conectividad o configuración de servicios.
Auditoría: Asegurarse de que solo los puertos necesarios estén accesibles.
Nivel de dificultad: Principiante a intermedio.

Cuando se tiene una expresión: modulo.funcion()
modulo(primer término): Es el modulo importado
funcion(segundo término): Es la clase o función definida dentro del módulo.

¿Cómo implementar funciones en interfaces gráficas?
"""

import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print("Your IP is: ", IP)
target = input("Enter an IP to scan: ")
# Cambia el rango de puertos a escanear (por ejemplo, 1-1024)
PORT_START = 1
PORT_END = 1024

def port_scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # Opcional: para que no tarde mucho en puertos cerrados
    try:
        s.connect((target, port))
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        s.close()
        return False

for x in range(PORT_START, PORT_END):
    if port_scanner(x):
        print(f"Port {x} is open.")