print("temperatures and facts about the moon".title()) # el metodo title convierte la primera en mayuscula
###############
heading = "teMperatures and facts about tHe Moon"
heading_upper = heading.upper()
print(heading_upper)

# .upper() todas mayusculas
# .lower() todas minusculas

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split() #separa todo en comas
print(temperatures_list)
###################
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n') # separa solo donde se ubica ese caracter
print(temperatures_list)
##################
print("Moon" in "This text will describe facts and challenges with space travel") # saber si la palabra moon se encuentra en el texto siguiente
##################
print("Moon" in "This text will describe facts about the Moon")
########################
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon")) # saber en que ubicacion se encuentra la palabra moon, si no lo encuentra se marca con un -1
##########################
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars")) # .find() si encuentra "mars" indica en que indice esta
#########################
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars")) # .count () uantas veces se repite la palabra 
print(temperatures.count("Moon"))
#####################
