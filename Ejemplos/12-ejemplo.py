rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(key, ":", rainfall[key], "cm") # una forma de escribirlo
    print(f'{key}: {rainfall[key]}cm') # otra forma de escribirlo

