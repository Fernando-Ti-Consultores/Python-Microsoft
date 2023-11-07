from time import sleep

new_planet = ""
lista_planeta = []

while new_planet.lower() != "listo":
    sleep(0.5)
    if new_planet:
        lista_planeta.append(new_planet)
    new_planet = input("ingrese planeta cuando finalice ingrese listo: ")

for planets in lista_planeta:
    print(planets)
    sleep(0.5)

