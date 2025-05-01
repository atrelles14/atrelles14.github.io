import os
import sys

def renombrar_archivos(directorio):
    """
    Renombra todos los archivos en el directorio especificado a Lourdes1, Lourdes2, etc.
    conservando la extensión original de cada archivo.
    """
    # Verificar si el directorio existe
    if not os.path.isdir(directorio):
        print(f"Error: El directorio '{directorio}' no existe.")
        return
    
    # Obtener todos los archivos en el directorio (excluyendo subdirectorios)
    archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
    
    # Ordenar los archivos (opcional)
    archivos.sort()
    
    # Contador para numerar los archivos
    contador = 1
    
    # Renombrar cada archivo
    for archivo in archivos:
        # Obtener la extensión del archivo original
        nombre_base, extension = os.path.splitext(archivo)
        
        # Crear el nuevo nombre
        nuevo_nombre = f"Lourdes{contador}{extension}"
        
        # Rutas completas
        ruta_original = os.path.join(directorio, archivo)
        ruta_nueva = os.path.join(directorio, nuevo_nombre)
        
        # Renombrar el archivo
        try:
            os.rename(ruta_original, ruta_nueva)
            print(f"Renombrado: {archivo} -> {nuevo_nombre}")
            contador += 1
        except Exception as e:
            print(f"Error al renombrar '{archivo}': {e}")

if __name__ == "__main__":
    # Si se proporciona un directorio como argumento, úsalo
    if len(sys.argv) > 1:
        directorio = sys.argv[1]
    else:
        # Si no, usa el directorio actual
        directorio = "."
    
    print(f"Renombrando archivos en el directorio: {os.path.abspath(directorio)}")
    renombrar_archivos(directorio)
    print("Proceso completado.")