def distance_from_earth(destination):
    if destination == ("Moon"):
        return "238,855"
    else:
        return "Unable to compute to that destination"
    
print(distance_from_earth("Moon"))
#--------------

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(22, 33))

#-----------------
def porcentaje_de_numero(porcentaje, numero):
    resultado = (numero * porcentaje) / 100
    return resultado

print(porcentaje_de_numero(80, 1000))

#-------------
days_to_completes = days_to_complete(2355233, 1030)
print(round(days_to_completes))

# o puede ser asi tambien agregando una funcion a otra funcion
print(round(days_to_complete(2355233, 1030)))
