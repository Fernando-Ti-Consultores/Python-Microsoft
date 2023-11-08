rainfall = {
    'october': 3.5,
    'november': 4.2
}

for key in rainfall.keys():
#    print(key, ":", rainfall[key], "cm") # una forma de escribirlo
    print(f"{key}: {rainfall[key]}cm")

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

print(rainfall)
