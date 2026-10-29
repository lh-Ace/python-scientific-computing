temperature = 27
minimum_temperature = 18
maximum_temperature = 26
within_range = minimum_temperature <= temperature and temperature <= maximum_temperature
classification = ""

if within_range:
    classification = "Within range"
elif maximum_temperature < temperature:
    classification = "Above range"
else:
    classification = "Below range"

print("LABORATORY TEMPERATURE MONITOR")
print(f"Temperature: {temperature} °C")
print(f"Acceptable interval: {minimum_temperature}-{maximum_temperature} °C")
print(f"Within range: {within_range}")
print(f"Classification: {classification}")