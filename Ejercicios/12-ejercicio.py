new_planet = ""
lista_planeta = []

while new_planet != "listo":
    if new_planet:
        lista_planeta.append(new_planet)
    new_planet = input(""" ingresar planeta, al finalizar ingresar "listo" : """)
print(lista_planeta)

