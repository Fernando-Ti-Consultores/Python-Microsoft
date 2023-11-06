planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

number_of_planets = len(planets) # para ver la longitud de una lista
print("There are", number_of_planets, "planets in the solar system.")

planets.append("Pluto") # append agrega un nuevo elemento a la lista
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

planets.pop()  # Goodbye, Pluto (elimina el ultimo elemento)
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

print("The last planet is", planets[-1]) # -1 devuelve el ultimo de la lista
print("The penultimate planet is", planets[-2]) # -2 el penultimo de la lista y asi sucesivamente

jupiter_index = planets.index("Jupiter") # para buscar el indice en una lista
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

