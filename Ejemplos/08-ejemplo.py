planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
numero_planeta = planets[0:2]
print(numero_planeta)

planets_after_earth = planets[3:8]
print(planets_after_earth) 

planets_after_earth = planets[3:]
print(planets_after_earth)


amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons # se pueden sumar las listas
print("The regular satellite moons of Jupiter are", regular_satellite_moons)


amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort() # las ordena en orden alfabetico y si es lista de numero en orden numerico
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
regular_satellite_moons.sort(reverse=True)# para ordenanrlo inversamente
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
#usar sort modifica la lista actual



