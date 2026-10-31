def cooling_step(current_temperature, ambient_temperature, cooling_fraction):
    current_temperature = current_temperature + cooling_fraction * (ambient_temperature - current_temperature)
    return current_temperature


def simulate_trajectory(initial_temperature, ambient_temperature, cooling_fraction, steps):
    trajectory = [initial_temperature]
    for step in range(steps):
        initial_temperature = cooling_step(
            initial_temperature, 
            ambient_temperature, 
            cooling_fraction
            )
        trajectory.append(initial_temperature)

    return trajectory

conditions = {
    "initial_temperature" : 80,
    "ambient_temperature" : 20,
    "cooling_fraction" : 0.2,
    "steps" : 6
}

final_temperature = []
final_temperature.append(simulate_trajectory(
    conditions["initial_temperature"], 
    conditions["ambient_temperature"], 
    conditions["cooling_fraction"], 
    conditions["steps"]
    ))

mean = 0
for temperature in final_temperature[0]:
    mean += temperature

mean /= len(final_temperature[0])
print(mean)

conditions["initial_temperature"] = 10
final_temperature.append(simulate_trajectory(
    conditions["initial_temperature"], 
    conditions["ambient_temperature"], 
    conditions["cooling_fraction"], 
    conditions["steps"]
    ))
conditions["initial_temperature"] = 80

conditions["steps"] = 0
final_temperature.append(simulate_trajectory(
    conditions["initial_temperature"], 
    conditions["ambient_temperature"], 
    conditions["cooling_fraction"], 
    conditions["steps"]
    ))
conditions["steps"] = 3

conditions["cooling_fraction"] = 0
final_temperature.append(simulate_trajectory(
    conditions["initial_temperature"], 
    conditions["ambient_temperature"], 
    conditions["cooling_fraction"], 
    conditions["steps"]
    ))
conditions["cooling_fraction"] = 0.2

for trajectory in final_temperature:
    print(trajectory)
    print(len(trajectory))
    print(trajectory[0])
    print(trajectory[-1])

