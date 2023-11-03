name = "Ganymede"
planet = "Mars"
gravity = 1.43

#plantilla = """Gravity Facts about {name}\n--------------------------\nPlanet Name: {planet}\nGravity on {name}: {gravity} m/s2"""

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))

######################
# o puede ser asi tambien
template = f"""Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template)