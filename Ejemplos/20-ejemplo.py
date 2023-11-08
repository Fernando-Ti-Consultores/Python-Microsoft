# open("/path/to/mars.jpg")

try:
     open('config.txt')
except FileNotFoundError:
     print("No se pudo encontrar el archivo config.txt")