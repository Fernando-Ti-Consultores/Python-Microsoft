planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
que_planeta = input("ingrese un planeta con la primera letra mayuscula: ")

planeta_index = planetas.index(que_planeta)

print("el planeta mas cercano es ", planetas[planeta_index - 1], " y ", planetas[planeta_index + 1])


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
user_planet = input("Please enter the name of the planet (with a capital letter to start)")
planet_index = planets.index(user_planet)
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])