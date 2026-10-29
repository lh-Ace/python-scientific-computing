counter = 2

while counter < 9:
    print(counter)
    counter += 3

print("Finished")
print(counter)

position = 0
target = 14
step_size = 4

while position < target:
    position += step_size
    print(f"Position: {position} m")

print(f"Final position: {position} m")

position = 0
target = 16

while position < target:
    position += step_size
    print(f"Position: {position} m")

print(f"Final position: {position} m")

steps = 0
maximum_steps = 0

while steps < maximum_steps:
    steps += 1
    print(f"Step {steps}")

print(f"Total steps: {steps}")