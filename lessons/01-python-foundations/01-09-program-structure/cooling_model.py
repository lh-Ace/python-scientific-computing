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
