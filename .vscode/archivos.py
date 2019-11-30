# Lista de paises https://paste.ee/p/0EvRF
# Guardar en un archivo llamado paises.txt

archivo = open("paises.txt", "r")

for linea in archivo:
    print(linea.strip())

archivo.close