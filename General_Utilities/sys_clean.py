import os
import shutil
import ctypes


def sys_clean():

    dir = [
        'C:/Windows/Prefetch',
        'C:/Windows/Temp',
        'C:/Users/admin/AppData/Local/Temp',
        'C:/Users/admin/AppData/Roaming/Code/Cache',
        'C:/Users/admin/AppData/Roaming/Code/CachedData',
    ]

    def borrar_contenido_directorio(ruta_directorio):
        import os
        # Verificar si la ruta es un directorio válido
        if os.path.isdir(ruta_directorio):
            num0 = len(os.listdir(ruta_directorio))
            # Eliminar todos los archivos y subdirectorios dentro del directorio
            for nombre_archivo in os.listdir(ruta_directorio):
                ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
                try:
                    if os.path.isfile(ruta_archivo):
                        os.remove(ruta_archivo)
                    elif os.path.isdir(ruta_archivo):
                        shutil.rmtree(ruta_archivo)                
                except Exception as e:
                    print(e)
        else:
            print("La ruta especificada no es un directorio válido.")   
        num1 = len(os.listdir(ruta_directorio))
        numr = num0 - num1  
        return numr

    # Ejemplo de uso
    for i in dir:
        numr = borrar_contenido_directorio(i)
        print(f'Remociones de {i}: {numr}')
    
    input('Presione un tecla para continuar: ')


def empty_recycle_bin():
    try:
        # Obtener la ruta de la papelera de reciclaje en Windows
        recycle_bin = ctypes.c_wchar_p(os.path.expanduser("~\RecycleBin"))
         # Eliminar todos los archivos de la papelera de reciclaje
        for root, _, files in os.walk(recycle_bin.value):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
        print("La papelera de reciclaje se ha vaciado correctamente.")
    except Exception as e:
        print("Ocurrió un error al vaciar la papelera de reciclaje:", str(e))


