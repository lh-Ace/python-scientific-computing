print("Starting experiment")

import measurement_tools

result = measurement_tools.offset_reading(10, 5)
print(f"Result: {result}")

temperatures = [17, 18, 26, 27]
temperature_status = {}
for temperature in temperatures:
    temperature_status[temperature] = measurement_tools.within_limits(temperature, 18, 26)

for temperature in temperature_status:
    print(f"Temperature {temperature}: {temperature_status[temperature]}")
print("Experiment complete")

import measurement_tools
from measurement_tools import within_limits
import measurement_tools as mt

print(f"Offset: {measurement_tools.offset_reading(15, 5)}")
print(f"Test 1: {within_limits(24, 18, 26)}")
print(f"Test 2: {mt.within_limits(29, 18, 26)}")
