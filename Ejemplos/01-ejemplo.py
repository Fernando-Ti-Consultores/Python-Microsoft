temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
######################3
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric(): # puede buscar numero en la cadena y mostrarlo .isdecimal() para decimal
        print(item) # los numero negativos no funcionan
##################
print("-60".startswith('-')) # para detectar negativos o detecta el caracte al inicio
###################
if "30 C".endswith("C"): # .endswith() detecta si se encuentra el caracter alfinal
    print("This temperature is in Celsius")
    ##############
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
# .replace() reemplaza una palabra por otra
################
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)
#################
text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower()) # se tiene que cambiar todo a minusculas para encontrar
###################
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts)) # '' se usa para unir todos los elementos de la lista
######################
