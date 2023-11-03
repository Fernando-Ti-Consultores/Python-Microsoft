texto = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

oracion = texto.split(". ")
for lista in oracion:
    if "temperature" in lista:
        print(lista)
#######################
texto = "Las niñas jugaban en el campo cuando, asustadas por un ruido de árboles cayendo, comenzaron a correr a toda velocidad, de modo que en pocos minutos ya estaban en casa de su abuela. La pelota cayó detrás de la verja y los niños ya no podrán recuperarla."

oracion = texto.split(",")
for lista in oracion:
    if "casa" in lista:
        print(lista)