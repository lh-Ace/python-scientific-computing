def kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

first_energy = kinetic_energy(2, 3)
second_energy = kinetic_energy(5, 4)

print(f"First energy: {first_energy}")
print(f"Second energy: {second_energy}")

combined_energy = first_energy + second_energy

print(f"Combined energy: {combined_energy}")

def potential_energy(mass, height, gravity=9.81):
    return mass * height * gravity

earth_1 = potential_energy(2, 5)
moon = potential_energy(2, 5, 1.62)
earth_2 = potential_energy(height=10, mass=3)

print(f"Earth: {earth_1:.2f}")
print(f"Moon: {moon:.2f}")
print(f"Earth: {earth_2:.2f}")

def safe_mean(total, count):
    if count == 0:
        return None
    return total / count

result = safe_mean(30, 5)
if result is None:
    print("Cannot calculate a mean without observations")
else:
    print(result)

result = safe_mean(0, 0)
if result is None:
    print("Cannot calculate a mean without observations")
else:
    print(result)

result = safe_mean(45, 9)
if result is None:
    print("Cannot calculate a mean without observations")
else:
    print(result)

temperature = 80

def update_temperature(temperature):
    temperature += 10
    print(f"Inside: {temperature}")
    return temperature

new_temperature = update_temperature(temperature)

print(f"Original: {temperature}")
print(f"Updated: {new_temperature}")
