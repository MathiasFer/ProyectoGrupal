import os
import time
from send2trash import send2trash

def eliminar_archivos_temporales(ruta_temp, tamano_limite):
    archivos_eliminados = []
    archivos_no_eliminados = []

    try:
        for archivo in os.listdir(ruta_temp):
            ruta_archivo = os.path.join(ruta_temp, archivo)
            if os.path.isfile(ruta_archivo) and os.path.getsize(ruta_archivo) > tamano_limite:
                time.sleep(1)  # Espera 1 segundo antes de enviar a la papelera
                try:
                    ruta_archivo_normalizada = os.path.normpath(ruta_archivo)
                    send2trash(ruta_archivo_normalizada)
                    print(f"Se movió a la papelera el archivo: {ruta_archivo_normalizada}")
                    archivos_eliminados.append(archivo)
                except Exception as e:
                    print(f"No se pudo enviar a la papelera el archivo {ruta_archivo}. Error: {e}")
                    archivos_no_eliminados.append(archivo)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    print("\nArchivos movidos a la papelera:")
    for archivo in archivos_eliminados:
        print(archivo)

    print("\nArchivos no movidos a la papelera:")
    for archivo in archivos_no_eliminados:
        print(archivo)

    print(f"\nTotal de archivos movidos a la papelera: {len(archivos_eliminados)}")
    print(f"Total de archivos no movidos a la papelera: {len(archivos_no_eliminados)}")

if _name_ == "_main_":
    carpeta_temp = input("Ingresa la ruta de tu carpeta temp (presiona Enter para usar la carpeta por defecto): ") or "C:/Users/juanm/AppData/Local/Temp"
    tamano_limite = int(input("Ingresa el tamaño límite para eliminar archivos (en bytes): ") or 74000)

    eliminar_archivos_temporales(carpeta_temp, tamano_limite)
