import socket
from datetime import datetime

def validar_ip(ip):
    """Valida que la dirección ingresada sea una IPv4 válida."""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def escanear_puerto(ip, puerto, timeout=0.5):
    """Comprueba si un puerto TCP está abierto."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        resultado = sock.connect_ex((ip, puerto))
        return resultado == 0
    except (socket.timeout, socket.error):
        return False
    finally:
        sock.close()

def main():
    print("=" * 55)
    print("             ESCÁNER DE PUERTOS TCP")
    print("=" * 55)
    print("Uso exclusivo en equipos propios, máquinas virtuales")
    print("o laboratorios/redes con autorización.\n")

    # 1. Ingresar IP
    while True:
        ip = input("IP: ").strip()
        if validar_ip(ip):
            break
        print("Error: ingrese una dirección IPv4 válida. Ejemplo: 127.0.0.1")

    # 2. Ingresar puerto inicial
    while True:
        try:
            puerto_inicial = int(input("Desde: "))
            if 1 <= puerto_inicial <= 65535:
                break
            print("El puerto debe estar entre 1 y 65535.")
        except ValueError:
            print("Error: ingrese un número entero.")

    # 3. Ingresar puerto final
    while True:
        try:
            puerto_final = int(input("Hasta: "))
            if 1 <= puerto_final <= 65535 and puerto_final >= puerto_inicial:
                break
            print("El puerto final debe ser mayor o igual al inicial y estar entre 1 y 65535.")
        except ValueError:
            print("Error: ingrese un número entero.")

    total = puerto_final - puerto_inicial + 1
    puertos_abiertos = []

    print("\n" + "-" * 55)
    print("Escaneando...")
    print("-" * 55)

    inicio = datetime.now()

    # 4. Ejecutar el escaneo
    for puerto in range(puerto_inicial, puerto_final + 1):
        if escanear_puerto(ip, puerto):
            puertos_abiertos.append(puerto)
            print(f"Puerto {puerto} - ABIERTO")

    fin = datetime.now()
    duracion = (fin - inicio).total_seconds()

    # 5 y 6. Mostrar resultados y resumen
    print("\n" + "=" * 55)
    print("                 RESUMEN DE RESULTADOS")
    print("=" * 55)
    print(f"IP analizada:      {ip}")
    print(f"Rango analizado:   {puerto_inicial}-{puerto_final}")
    print(f"Puertos analizados:{total}")
    print(f"Puertos abiertos:  {len(puertos_abiertos)}")
    print(f"Tiempo empleado:   {duracion:.2f} segundos")

    if puertos_abiertos:
        print("Puertos abiertos:  " + ", ".join(map(str, puertos_abiertos)))
    else:
        print("Puertos abiertos:  Ninguno encontrado en el rango.")

    print("=" * 55)

if __name__ == "__main__":
    main()
