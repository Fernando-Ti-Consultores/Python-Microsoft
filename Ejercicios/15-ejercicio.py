planet_moons = {
    "mercury": 0,
    "venus": 0,
    "earth": 1,
    "mars": 2,
    "jupiter": 79,
    "saturn": 82,
    "uranus": 27,
    "neptune": 14,
    "pluto": 5,
    "haumea": 2,
    "makemake": 1,
    "eris": 1
}

moons = planet_moons.values()
print(moons)

total_planets = len(planet_moons.keys())
print(f"el total de planetas {total_planets}")

total_moons = 0

for promedio in planet_moons.values():
    total_moons = promedio + total_moons

print(f"el total de lunas {total_moons}")

resultado = total_moons / total_planets

print(f"el promedio es {resultado}")
    

