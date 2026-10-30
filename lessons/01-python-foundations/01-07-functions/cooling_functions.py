def cooling_step(current_temperature, ambient_temperature, cooling_fraction):
    current_temperature = current_temperature + cooling_fraction * (ambient_temperature - current_temperature)
    return current_temperature

def simulate_cooling(initial_temperature, ambient_temperature, cooling_fraction, steps):
    current_temperature = initial_temperature
    for _ in range(steps):
        current_temperature = cooling_step(current_temperature, ambient_temperature, cooling_fraction)

    return current_temperature

initial_temperature = 80
ambient_temperature = 20
cooling_fraction = 0.2
steps = 6

final_temperature = simulate_cooling(initial_temperature, ambient_temperature, cooling_fraction, steps)
print(f"Case 1: {final_temperature:.2f}")

initial_temperature = 10
ambient_temperature = 20
cooling_fraction = 0.2
steps = 6

final_temperature = simulate_cooling(initial_temperature, ambient_temperature, cooling_fraction, steps)
print(f"Case 2: {final_temperature:.2f}")

initial_temperature = 80
ambient_temperature = 20
cooling_fraction = 0.2
steps = 0

final_temperature = simulate_cooling(initial_temperature, ambient_temperature, cooling_fraction, steps)
print(f"Case 3: {final_temperature:.2f}")

initial_temperature = 80
ambient_temperature = 20
cooling_fraction = 0
steps = 6

final_temperature = simulate_cooling(initial_temperature, ambient_temperature, cooling_fraction, steps)
print(f"Case 4: {final_temperature:.2f}")

steps = 0

final_temperature = cooling_step(80, 20, 0.2)
print(f"Case 5: {final_temperature:.2f}")