import os
import shutil

# Función para listar archivos en un directorio
def listar_archivos():
    directorio = os.getcwd()  # Usar el directorio actual
    try:
        archivos = os.listdir(directorio)
        print(f"Contenido del directorio actual ('{directorio}'):")
        for archivo in archivos:
            print(f" - {archivo}")
    except PermissionError:
        print("No tienes permiso para acceder al directorio actual.")

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
def copiar_archivo(origen, log_copias):
    destino = os.path.join(os.getcwd(), os.path.basename(origen))  # Path actual + nombre del archivo
    if os.path.exists(origen):
        shutil.copy(origen, destino)
        print(f"Archivo '{origen}' copiado a '{destino}'.")
        log_copias.append(origen)  # Modifica la lista (llamada por referencia)
    else:
        print(f"El archivo '{origen}' no existe.")

# Programa principal
def main():
    log_copias = []  # Lista para registrar archivos copiados
    while True:
        print("\nGestor de Archivos:")
        print("1. Listar archivos")
        print("2. Renombrar archivo")
        print("3. Eliminar archivo")
        print("4. Copiar archivo")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            original = input("Nombre del archivo a renombrar: ")
            nuevo = input("Nuevo nombre: ")
            renombrar_archivo(original, nuevo)
        elif opcion == "3":
            archivo = input("Nombre del archivo a eliminar: ")
            eliminar_archivo(archivo)
        elif opcion == "4":
            origen = input("Archivo a copiar: ")
            copiar_archivo(origen, log_copias)
            print("Archivos copiados:", log_copias)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

main()
