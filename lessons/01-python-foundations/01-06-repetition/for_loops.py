# range(start, stop, step)

for number in range(3, 16, 4):
    print(number)

for number in range(12, 0, -3):
    print(number)

for number in range(0, 6, 1):
    print(number)

total = 0
count = 0
sum_of_squares = 0

for number in range(2, 11, 2):
    total += number
    count += 1
    sum_of_squares += number ** 2
    
    print(f"Count: {count}")
    print(f"Sum: {total}")

print(f"Final count: {total}")
print(f"Sum of squares: {sum_of_squares}")
print(f"Arithmetic mean: {total / count:.1f}")

total = 0

for number in range(1, 11):
    if (number % 3) == 0:
        continue
    if number == 8:
        break
    print(number)
    total += number

print(total)
