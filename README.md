# APAP - All Ports Are Bastards

**APAP** es una herramienta en Python para detectar conexiones de red sospechosas en tu sistema, basada en la monitorización de puertos remotos que podrían indicar actividad maliciosa.

El programa tiene una interfaz tipo consola con banner ASCII y menú interactivo, inspirado en herramientas de Kali Linux como Metasploit o Kiwi.

---

## Características

- Escaneo de conexiones activas establecidas
- Identificación de puertos remotos sospechosos (puedes configurar la lista)
- Interfaz CLI sencilla con menú y banner
- Fácil de usar y modificar para tus necesidades

---

## Requisitos

- Python 3.6+
- Módulos Python: `psutil`, `pyfiglet`, `termcolor`

Puedes instalar las dependencias con:

```bash
pip install psutil pyfiglet termcolor
