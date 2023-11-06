# Aritmeticas
print(5 + 15) # suma 5 + 15
print(5 - 15) # resta 5 - 15
print(5 * 15) # multiplica 5 * 15
print(15 / 5) # divide 15 / 5
print(5 ** 3) # 5 elevado a 3 (5*5*5)
print(10 % 3) # el modulo lo que resta o sobra en una division osea 1

seconds = 1042
display_minutes = 1042 // 60 # el  // se usa cuando se necesita redondear la division
#en este caso se quiere sacar de los segundo la cantidad de min
#------------
# El primer paso consiste en determinar el número de minutos que hay en 1042 segundos. 
# Con 60 segundos en un minuto, puede dividir por 60 y obtener una respuesta de 17.3666667.
#  El número que le interesa simplemente es 17. Se recomienda redondear hacia abajo, usando 
# lo que se conoce como división de múltiplo inferior. Para realizar una división de este tipo en Python, debe utilizar //.
print(display_minutes)
""" Orden de las operaciones
Python respeta el orden de las operaciones en matemáticas. El orden de las operaciones determina que las expresiones se deben evaluar en este orden:

Paréntesis
Exponentes
Multiplicación y división
Suma y resta """

