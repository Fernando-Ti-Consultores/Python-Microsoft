earth_name = 'Earth'
earth_moons = 1

jupiter_name = 'Jupiter'
jupiter_moons = 79

# almacenar biblioteca de datos en una variable (varias variables en una)
planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('moons')) # es una forma de consultar una biblioteca de una variable


print(planet['moons']) # esta es la forma mas utilizada y mas sencilla

planet.update({'name': 'Makemake'}) # modifica una variable
print(planet["name"])

planet['name'] = 'Makesito' # este modifica de una forma mas sencilla
print(planet["name"])

planet['orbital period'] = 4333 # si se quiere agregar a la biblioteca

planet.pop('orbital period') # para eliminarlo

# se agrega una biblioteca dentro de otra
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

print(planet["diameter (km)"]["polar"]) # hacer una llamada a la variable de una biblioteca dentro de otra

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')