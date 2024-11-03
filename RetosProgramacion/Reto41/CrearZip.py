### Crear un zip con un fichero ###

import zipfile
import os
import shutil
from datetime import datetime

# Pedir el nombre del fichero 
nombre_fichero_zip=input ("Nombre del fichero .ZIP: ")
nombre_fichero_a_comprimir=input ("Nombre del fichero a comprimir: ")

fichero_comprimido=zipfile.ZipFile(nombre_fichero_zip, mode="a")
fichero_comprimido.write(nombre_fichero_a_comprimir)

