import errno
import os
import shutil
import time

def eliminar_archivos_temporales(tamaño_maximo):
    try:
        carpeta_temporal = os.environ.get('TEMP') or os.environ.get('TMP') or '/tmp'

        archivos_temporales = []

        # Obtener la lista de archivos en la carpeta temporal
        for archivo in os.listdir(carpeta_temporal):
            ruta_completa = os.path.join(carpeta_temporal, archivo)

            try:
                # Verificar si es un archivo temporal basado en criterios (ajusta según tus necesidades)
                if os.path.isfile(ruta_completa) and os.path.getsize(ruta_completa) < tamaño_maximo:
                    archivos_temporales.append(ruta_completa)
            except Exception as e:
                print(f"Error al verificar el archivo {ruta_completa}: {str(e)}")

        # Eliminar los archivos temporales identificados
        for archivo_temporal in archivos_temporales:
            try:
                os.remove(archivo_temporal)
                print(f"Eliminado: {archivo_temporal}")
            except OSError as e:
                # Omitir el archivo si se encuentra en uso
                if e.errno == errno.EACCES or e.errno == errno.EBUSY:
                    print(f"Omitido (en uso): {archivo_temporal}")
                else:
                    print(f"Error al eliminar {archivo_temporal}: {str(e)}")

        # Intentar eliminar directorios (esto incluirá subdirectorios)
        try:
            shutil.rmtree(carpeta_temporal)
            print(f"Eliminado directorio completo: {carpeta_temporal}")
        except Exception as e:
            print(f"Error al eliminar directorio: {str(e)}")

    except Exception as e:
        print(f"Error al eliminar archivos temporales: {str(e)}")

def programar_eliminacion_programada(tamaño_maximo, intervalo_tiempo):
    while True:
        # Llamar a la función para eliminar archivos temporales
        eliminar_archivos_temporales(tamaño_maximo)

        # Esperar el intervalo de tiempo antes de la próxima ejecución
        time.sleep(intervalo_tiempo)

# Configuración
tamaño_maximo_archivo = 77 # Tamaño máximo en kilobytes (ajusta según tus necesidades)
intervalo_tiempo_eliminar = 3600 # Intervalo de tiempo en segundos (ajusta según tus necesidades)

# Llamar a la función para la eliminación programada
programar_eliminacion_programada(tamaño_maximo_archivo, intervalo_tiempo_eliminar)