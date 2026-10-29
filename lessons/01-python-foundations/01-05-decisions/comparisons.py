score = 82
passing_score = 70
maximum_score = 100

print(f"Above passing score: {score >= passing_score}")
print(f"Maximum score: {score == maximum_score}")
print(f"Different than passing score: {score != passing_score}")
print(f"Above maximum score: {score > maximum_score}")
print(f"Below passing score: {score < passing_score}")

score = 70

print(f"Above passing score: {score >= passing_score}")
print(f"Maximum score: {score == maximum_score}")
print(f"Different tahn passing score: {score != passing_score}")
print(f"Above maximum score: {score > maximum_score}")
print(f"Below passing score: {score < passing_score}")

door_locked = True
power_online = True
pressure = 125
maximum_pressure = 120

print(f"Machine can start: {door_locked and power_online and pressure <= maximum_pressure}")
print(f"Requires attention: {not door_locked or pressure > maximum_pressure}")
print(f"Pressure safe: {not (pressure > maximum_pressure)}")

pressure = 120

print(f"Machine can start: {door_locked and power_online and pressure <= maximum_pressure}")
print(f"Requires attention: {not door_locked or pressure > maximum_pressure}")
print(f"Pressure safe: {not (pressure > maximum_pressure)}")