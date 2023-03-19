import os

# Obtiene la ruta de la carpeta actual
carpeta_actual = os.getcwd()
carpeta_actual += "\personas"
print(carpeta_actual)

# Itera sobre todos los archivos en la carpeta actual
for archivo in os.listdir(carpeta_actual):
    # Comprueba si el archivo es en realidad un archivo y no una carpeta
    if os.path.isfile(os.path.join(carpeta_actual, archivo)):
        # Imprime el nombre del archivo
        print(archivo)