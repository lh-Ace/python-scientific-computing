sensor = {
    "id" : "S-01",
    "temperature" : 22.0,
    "minimum" : 18,
    "maximum" : 26 
}

print(sensor.get("id"))
print(sensor.get("temperature"))

sensor["temperature"] = 27.0

if sensor["temperature"] < sensor["minimum"]:
    sensor["status"] = "Below range"
elif sensor["maximum"] < sensor["temperature"]:
    sensor["status"] = "Above range"
else:
    sensor["status"] = "Within range"

print(sensor.get("status", "Not recorded"))
print(sensor)
print("status" in sensor)
print(sensor.get("pressure", "Not recorded"))

for key in sensor:
    print(key, sensor[key])

reported_sensors = ["S-01", "S-03", "S-01", "S-04", "S-03", "S-05"]
unique_sensors = set(reported_sensors)

print(reported_sensors)
print(unique_sensors)

unique_sensors.add("S-06")
unique_sensors.discard("S-04")

inspection_sensors = {"S-03", "S-06", "S-08"}

print(unique_sensors | inspection_sensors)
print(unique_sensors & inspection_sensors)
print(unique_sensors - inspection_sensors)

print(f"S-03 in unique_sensors: {'S-03' in unique_sensors}")
print(f"S-04 in unique_sensors: {'S-04' in unique_sensors}")
print(f"Total reports: {len(reported_sensors)}")
print(f"Unique sensors: {len(unique_sensors)}")

readings = [17, 30, 31, 22, 18, 26, 27]
accepted_readings = []
rejected_readings = []
counts = {
    "accepted" : 0,
    "rejected" : 0
}

for reading in readings:
    if 18 <= reading <= 26:
        accepted_readings.append(reading)
        counts["accepted"] += 1
    else:
        rejected_readings.append(reading)
        counts["rejected"] += 1

print(f"Original list: {readings}")
print(f"Accepted Readings: {accepted_readings}")
print(f"Rejected Readings: {rejected_readings}")
print(f"Accepted Readings amount: {counts['accepted']}")
print(f"Rejected Readings amount: {counts['rejected']}")