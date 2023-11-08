def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""   "Fuel Report"
    main tank: {main_tank}
    external tank: {external_tank} 
    hydrogen tank: {hydrogen_tank}"""
    print(output)

generate_report(80, 70, 75)