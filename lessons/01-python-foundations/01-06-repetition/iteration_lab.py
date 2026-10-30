initial_temperature = 80
ambient_temperature = 20
cooling_fraction = 0.2
steps = 6

current_temperature = initial_temperature
print(f"Initial temperature: {initial_temperature:.2f} °C")
print(f"Ambient temperature: {ambient_temperature:.2f} °C")

for number in range(1, steps + 1):
    current_temperature = current_temperature + (cooling_fraction * (ambient_temperature - current_temperature))
    print(f"Step {number}: {current_temperature:.2f} °C")

print(f"Final temperature: {current_temperature:.2f} °C")

initial_temperature = 10
current_temperature = initial_temperature
print(f"Initial temperature: {initial_temperature:.2f} °C")
print(f"Ambient temperature: {ambient_temperature:.2f} °C")

for number in range(1, steps + 1):
    current_temperature = current_temperature + (cooling_fraction * (ambient_temperature - current_temperature))
    print(f"Step {number}: {current_temperature:.2f} °C")

print(f"Final temperature: {current_temperature:.2f} °C")
