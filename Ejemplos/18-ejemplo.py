def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
print(sequence_time(120))

#--------------

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

print(crew_members(tanks=1, day="Wednesday", pilots=3))
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", comand_pilot="Michael Collins")