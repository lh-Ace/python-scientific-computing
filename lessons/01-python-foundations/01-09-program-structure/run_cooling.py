import cooling_model

def main():
    conditions = {
        "initial_temperature" : 80,
        "ambient_temperature" : 20,
        "cooling_fraction" : 0.2,
        "steps" : 6
    }

    trajectories = []
    trajectories.append(cooling_model.simulate_trajectory(
        conditions["initial_temperature"], 
        conditions["ambient_temperature"], 
        conditions["cooling_fraction"], 
        conditions["steps"]
        ))

    mean = 0
    for temperature in trajectories[0]:
        mean += temperature

    mean /= len(trajectories[0])
    print(mean)

    conditions["initial_temperature"] = 10
    trajectories.append(cooling_model.simulate_trajectory(
        conditions["initial_temperature"], 
        conditions["ambient_temperature"], 
        conditions["cooling_fraction"], 
        conditions["steps"]
        ))
    conditions["initial_temperature"] = 80

    conditions["steps"] = 0
    trajectories.append(cooling_model.simulate_trajectory(
        conditions["initial_temperature"], 
        conditions["ambient_temperature"], 
        conditions["cooling_fraction"], 
        conditions["steps"]
        ))
    conditions["steps"] = 3

    conditions["cooling_fraction"] = 0
    trajectories.append(cooling_model.simulate_trajectory(
        conditions["initial_temperature"], 
        conditions["ambient_temperature"], 
        conditions["cooling_fraction"], 
        conditions["steps"]
        ))
    conditions["cooling_fraction"] = 0.2

    for trajectory in trajectories:
        print(trajectory)
        print(len(trajectory))
        print(trajectory[0])
        print(trajectory[-1])

if __name__ == "__main__":
    main()