from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())
# ------------
from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

# print(arrival_time()) # en este caso ya no se puede usar () vacio osea sin argumento es necesario escribir uno
print(arrival_time("Moon")) # como aqui

arrival_time("Orbit", hours=0.13)
