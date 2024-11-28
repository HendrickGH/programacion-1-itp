import os
import shutil

# Función para listar archivos en un directorio
def listar_archivos(directorio):
    try:
        archivos = os.listdir(directorio)
        print(f"Contenido de '{directorio}':")
        for archivo in archivos:
            print(f" - {archivo}")
    except FileNotFoundError:
        print("El directorio no existe.")
    except PermissionError:
        print("No tienes permiso para acceder al directorio.")

# Función para renombrar un archivo (llamada por valor)
def renombrar_archivo(nombre_original, nuevo_nombre):
    if os.path.exists(nombre_original):
        os.rename(nombre_original, nuevo_nombre)
        print(f"Renombrado: {nombre_original} -> {nuevo_nombre}")
    else:
        print(f"El archivo '{nombre_original}' no existe.")

# Función para eliminar un archivo (llamada por valor)
def eliminar_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
        print(f"Archivo '{nombre_archivo}' eliminado.")
    else:
        print(f"El archivo '{nombre_archivo}' no existe.")

# Función para copiar un archivo (llamada por valor y referencia)
def copiar_archivo(origen, destino, log_copias):
    if os.path.exists(origen):
        shutil.copy(origen, destino)
        print(f"Archivo '{origen}' copiado a '{destino}'.")
        log_copias.append(origen)  # Modifica la lista (llamada por referencia)
    else:
        print(f"El archivo '{origen}' no existe.")

# Función para mostrar estadísticas de disco
def estadisticas_disco():
    uso_disco = shutil.disk_usage("/")
    print(f"Espacio total: {uso_disco.total // (1024**3)} GB")
    print(f"Espacio usado: {uso_disco.used // (1024**3)} GB")
    print(f"Espacio libre: {uso_disco.free // (1024**3)} GB")

# Programa principal
def main():
    log_copias = []  # Lista para registrar archivos copiados
    while True:
        print("\nGestor de Archivos:")
        print("1. Listar archivos")
        print("2. Renombrar archivo")
        print("3. Eliminar archivo")
        print("4. Copiar archivo")
        print("5. Estadísticas de disco")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            directorio = input("Ingresa el directorio a listar: ")
            listar_archivos(directorio)
        elif opcion == "2":
            original = input("Nombre del archivo a renombrar: ")
            nuevo = input("Nuevo nombre: ")
            renombrar_archivo(original, nuevo)
        elif opcion == "3":
            archivo = input("Nombre del archivo a eliminar: ")
            eliminar_archivo(archivo)
        elif opcion == "4":
            origen = input("Archivo a copiar: ")
            destino = input("Destino: ")
            copiar_archivo(origen, destino, log_copias)
            print("Archivos copiados:", log_copias)
        elif opcion == "5":
            estadisticas_disco()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

main()
