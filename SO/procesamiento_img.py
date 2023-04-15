from multiprocessing import Pool, cpu_count
from PIL import Image, ImageFilter
import os
import time

input_dir = '/home/jhonier/Multiprocesamiento/val2017/'
output_dir = 'Multiprocesamiento/dataSet_procesado/'  # Directorio de sálida


def procesamiento(file):
    image = Image.open(input_dir + file)  # Ruta más nombre del archivo
    image = image.rotate(45, expand=True)
    image = image.filter(ImageFilter.GaussianBlur(2))
    image = image.transpose(1)  # Volter la imagen
    # Guardas los cambios en el directorio de sálida
    image.save(output_dir + file)


if not os.path.exists(output_dir):
    os.mkdir(output_dir)

list_files = os.listdir(input_dir)  # listdir(input_dir)

# Secuencial
start = time.time()
for file in list_files:
    procesamiento(file)
print('tiempo total serial: ', time.time()-start, '\n')

# Multiprocesamiento

start = time.time()
p = Pool(cpu_count())
p.map(procesamiento, list_files)
p.close()
print('Tiempo total paralelo: ', time.time() - start, '\n')