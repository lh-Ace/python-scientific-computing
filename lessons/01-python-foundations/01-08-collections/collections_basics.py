readings = [21.5, 22.0, 19.8]

print(readings[0])
print(readings[-1])

readings[1] = 22.2
readings.append(20.5)

print(readings)
print(len(readings))

for _ in range(len(readings)):
    print(readings[_])

measurements = [16, 18, 20, 22, 24]

mes1 = measurements[:3]
mes2 = measurements[-2:]
mes3 = measurements[::2]

print(mes1)
print(mes2)
print(mes3)

alias = measurements
sliced = measurements[:]

alias[1] = 19
sliced[0] = 99

print(measurements)
print(alias)
print(sliced)

limits = (18, 26)
print(limits[0])
print(limits[1])