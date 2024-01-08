import os
import time
from send2trash import send2trash

def verificar_tipo_archivo(ruta_archivo, tipo_archivo):
    if tipo_archivo == "Internet":
        extensiones_internet = [".html", ".htm", ".css", ".js", ".jpg", ".png", ".gif"]
        return any(ruta_archivo.lower().endswith(ext) for ext in extensiones_internet)
    elif tipo_archivo == "Sistema":
        extensiones_sistema = [".sys", ".dll", ".exe", ".ini", ".sys", ".log"]
        return any(ruta_archivo.lower().endswith(ext) for ext in extensiones_sistema)
    elif tipo_archivo == "Apps":
        extensiones_apps = [".app", ".exe", ".dll", ".dat"]
        return any(ruta_archivo.lower().endswith(ext) for ext in extensiones_apps)
    elif tipo_archivo == "Personalizado":
        extensiones_personalizadas = [".puff", ".txt" , ".tmp"]
        return any(ruta_archivo.lower().endswith(ext) for ext in extensiones_personalizadas)
    else:
        return True  # Eliminar cualquier tipo de archivo si no se especifica un tipo

def enviar_a_papelera(ruta_archivo):
    try:
        ruta_archivo_normalizada = os.path.normpath(ruta_archivo)
        send2trash(ruta_archivo_normalizada)
        return True
    except Exception as e:
        print(f"Error al enviar a la papelera el archivo {ruta_archivo}. Error: {e}")
        return False

def mostrar_resultados(archivos_eliminados, archivos_no_eliminados):
    print("\nArchivos movidos a la papelera:")
    for archivo in archivos_eliminados:
        print(archivo)

    print("\nArchivos no movidos a la papelera:")
    for archivo in archivos_no_eliminados:
        print(archivo)

    print(f"\nTotal de archivos movidos a la papelera: {len(archivos_eliminados)}")
    print(f"Total de archivos no movidos a la papelera: {len(archivos_no_eliminados)}")

def eliminar_archivos_por_tipo(ruta_temp, tamano_limite, tipo_archivo):
    archivos_eliminados = []
    archivos_no_eliminados = []

    try:
        for archivo in os.listdir(ruta_temp):
            ruta_archivo = os.path.join(ruta_temp, archivo)

            if os.path.isfile(ruta_archivo) and os.path.getsize(ruta_archivo) > tamano_limite:
                if verificar_tipo_archivo(ruta_archivo, tipo_archivo):
                    time.sleep(1)  # Espera 1 segundo antes de enviar a la papelera
                    if enviar_a_papelera(ruta_archivo):
                        print(f"Se movió a la papelera el archivo: {ruta_archivo}")
                        archivos_eliminados.append(archivo)
                    else:
                        print(f"No se pudo enviar a la papelera el archivo {ruta_archivo}")
                        archivos_no_eliminados.append(archivo)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    mostrar_resultados(archivos_eliminados, archivos_no_eliminados)

if __name__ == "__main__":
    carpeta_temp = input("Ingresa la ruta de tu carpeta temp (presiona Enter para usar la carpeta por defecto): ") or "C:/Users/FING~1.LAB/AppData/Local/Temp"
    tamano_limite = int(input("Ingresa el tamaño límite para eliminar archivos (en bytes): ") or 1000)

    print("\nTipos de archivos disponibles:")
    print("1. Internet")
    print("2. Sistema")
    print("3. Apps")
    print("4. Personalizado (.puff, .txt)")
    print("5. Todos (ninguna selección)")

    opcion_tipo_archivo = input("Seleccione el tipo de archivo a eliminar (1-5): ")
    
    if opcion_tipo_archivo == "1":
        tipo_archivo = "Internet"
    elif opcion_tipo_archivo == "2":
        tipo_archivo = "Sistema"
    elif opcion_tipo_archivo == "3":
        tipo_archivo = "Apps"
    elif opcion_tipo_archivo == "4":
        tipo_archivo = "Personalizado"
    else:
        tipo_archivo = "Todos"

    eliminar_archivos_por_tipo(carpeta_temp, tamano_limite, tipo_archivo)

