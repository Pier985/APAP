#!/usr/bin/env python3

import psutil
import pyfiglet
from termcolor import cprint

# =======================
# 🔥 BANNER PRINCIPAL
# =======================
def mostrar_banner():
    banner = pyfiglet.figlet_format("APAP")
    cprint(banner, "red")
    cprint("All Ports Are Bastards", "white", attrs=["bold"])
    cprint("[🔍] Detección de conexiones sospechosas - by Pier985", "yellow")
    print("-" * 60)

# =======================
# 🚨 DETECTOR DE PUERTOS SOSPECHOSOS
# =======================
def detectar_conexiones_sospechosas():
    # Lista de puertos que consideramos sospechosos (puedes modificar)
    puertos_sospechosos = [6666, 1337, 4444, 31337, 12345]

    conexiones = psutil.net_connections()

    hay_sospechosas = False

    for conn in conexiones:
        if conn.status == 'ESTABLISHED' and conn.raddr:
            pid = conn.pid
            local = f"{conn.laddr.ip}:{conn.laddr.port}"
            remota = f"{conn.raddr.ip}:{conn.raddr.port}"
            puerto_remoto = conn.raddr.port

            if puerto_remoto in puertos_sospechosos:
                cprint(f"\n[!] ⚠️ CONEXIÓN SOSPECHOSA DETECTADA:", "red")
                cprint(f"    → PID: {pid} | Local: {local} | Remota: {remota}", "red", attrs=["bold"])
                hay_sospechosas = True

    if not hay_sospechosas:
        cprint("\n[✔] No se han detectado conexiones sospechosas.", "green")

# =======================
# 🧭 MENÚ PRINCIPAL
# =======================
def menu():
    while True:
        print("\n[1] Escanear conexiones activas")
        print("[2] Salir")
        opcion = input("\n> ")

        if opcion == "1":
            detectar_conexiones_sospechosas()
        elif opcion == "2":
            cprint("\n[+] Cerrando APAP...", "cyan")
            break
        else:
            cprint("[!] Opción no válida. Intenta de nuevo.", "red")

# =======================
# 🚀 MAIN
# =======================
if __name__ == "__main__":
    mostrar_banner()
    menu()
