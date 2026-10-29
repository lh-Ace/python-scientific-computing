battery_level = 15
minimum_level = 20

if battery_level < minimum_level:
    print("Battery low")
else:
    print("Battery sufficient")

print("Battery check complete")

battery_level = 20

if battery_level < minimum_level:
    print("Battery low")
else:
    print("Battery sufficient")

print("Battery check complete")

battery_level = 25

if battery_level < minimum_level:
    print("Battery low")
else:
    print("Battery sufficient")

print("Battery check complete")

cpu_usage = 82

if 90 <= cpu_usage:
    print("Critical")
elif 75 <= cpu_usage:
    print("High")
elif 40 <= cpu_usage:
    print("Moderate")
else:
    print("Low")

reading = 18

if reading < 18:
    print("Below range")
elif reading > 26:
    print("Above range")
else:
    print("Within range")