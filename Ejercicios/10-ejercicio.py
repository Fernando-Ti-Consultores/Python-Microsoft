planets = ["Mercurio", "Venus", "Tierra", "Martes", "Júpiter", "Saturno", "Urano", "Neptuno"]

planeta = len(planets)

print("hay", planeta, "planetas")

planets.append("pluto")
planeta2 = len(planets)

print("mentira, hay", planeta2, "planetas ahora")

print("el ultimo planeta es", planets[-1])