# Create the variable for user input
user_input = "" # crea la variable para la entrada del usuario
# Create the list to store the values
inputs = [] # la lista donde se guardan los datos ingresados

# The while loop
while user_input.lower() != "done":
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done: ')

print(inputs)