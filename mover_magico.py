}import os
import shutil

# Ruta de origen y destino
origen = 'archivos_a_mover'
destino = 'archivos_movedizos'

# Crear carpeta destino si no existe
if not os.path.exists(destino):
    os.mkdir(destino)

# Listar archivos en la carpeta de origen
archivos = os.listdir(origen)

# Mover cada archivo
for archivo in archivos:
    origen_archivo = os.path.join(origen, archivo)
    destino_archivo = os.path.join(destino, archivo)

    if os.path.isfile(origen_archivo):
        shutil.move(origen_archivo, destino_archivo)
        print(f"✨ {archivo} fue movido mágicamente.")