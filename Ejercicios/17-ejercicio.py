def fuel_report(fuel_tanks, value):
    fuel = f"{fuel_tanks} : {value}"
    return fuel

print(fuel_report("pelo", 8))

def fuel_report2(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report2(main=50, external=100, emergency=60)
