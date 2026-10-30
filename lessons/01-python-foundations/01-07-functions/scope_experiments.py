def adjust_measurement(measurement, offset):
    measurement += offset
    print(measurement)
    return measurement

measurement = 12
adjusted = adjust_measurement(measurement, 5)
print(measurement)
print(adjusted)

new_adjusted = adjust_measurement(adjusted, -3)
print(measurement)
print(adjusted)
print(new_adjusted)

def scale_measurement(reading, factor=2):
    if factor < 0:
        return None

    scaled = reading * factor
    print(f"Scaled: {scaled}")
    
    return scaled


result = scale_measurement(4, 3)

print(f"Result: {result}")
print(result + 1)

print(scale_measurement(5))
print(scale_measurement(4, -1))